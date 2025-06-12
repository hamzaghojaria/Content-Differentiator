let uploadedFile = null;
let previewData = [];

// Hide full-page loader when page is fully loaded
window.onload = function() {
    document.getElementById("pageLoader").style.display = "none";
};

async function uploadFile() {
    const fileInput = document.getElementById("fileInput").files[0];
    if (!fileInput) {
        alert("Please select a file!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput);

    try {
        const response = await fetch("/preview/", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        if (response.ok && result.preview) {
            uploadedFile = fileInput;
            previewData = result.preview;
            populateTable(result.preview);
            populateDropdowns(result.preview);
        } else {
            alert("Error: " + (result.detail || "Failed to process file."));
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to upload file.");
    }
}




function populateTable(data) {
    const table = document.getElementById("previewTable");
    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = "<tr><td>No data available</td></tr>";
        return;
    }

    const headers = Object.keys(data[0]);
    let thead = "<thead><tr>" + headers.map(h => `<th>${h}</th>`).join('') + "</tr></thead>";
    let tbody = "<tbody>" + data.map(row =>
        "<tr>" + headers.map(h => `<td>${row[h] || ""}</td>`).join('') + "</tr>"
    ).join('') + "</tbody>";

    table.innerHTML = thead + tbody;
}




function populateDropdowns(data) {
    if (data.length === 0) return;

    const columns = Object.keys(data[0]);
    const column1Select = document.getElementById("column1");
    const column2Select = document.getElementById("column2");

    column1Select.innerHTML = columns.map(col => `<option value="${col}">${col}</option>`).join('');
    column2Select.innerHTML = columns.map(col => `<option value="${col}">${col}</option>`).join('');
}



async function processFile() {
    if (!uploadedFile) {
        alert("Please upload a file first!");
        return;
    }

    const column1 = document.getElementById("column1").value;
    const column2 = document.getElementById("column2").value;

    if (!column1 || !column2 || column1 === column2) {
        alert("Please select two different columns!");
        return;
    }

    const formData = new FormData();
    formData.append("file", uploadedFile);
    formData.append("column1", column1);
    formData.append("column2", column2);

    console.log("Sending FormData:", [...formData.entries()]);

    // Hide the download button when starting a new process
    document.getElementById("downloadSection").style.display = "none";

    // Show progress bar loader
    document.getElementById("progressBar").style.display = "block";

    try {
        const response = await fetch("/content-difference/", {
            method: "POST",
            body: formData
        });

        // Hide progress bar loader
        document.getElementById("progressBar").style.display = "none";

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Server Error: ${errorText}`);
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        document.getElementById("downloadLink").href = url;
        document.getElementById("downloadSection").style.display = "block";

    } catch (error) {
        document.getElementById("progressBar").style.display = "none";
        console.error("Error:", error);
        alert("Failed to process file: " + error.message);
    }
}