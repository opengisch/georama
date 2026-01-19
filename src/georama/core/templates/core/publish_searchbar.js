        // Filter the tables when the page loads
        document.addEventListener("DOMContentLoaded", function () {
            const tableFilter = document.getElementById("tableFilter");
            const datasetTabsContent = document.getElementById("datasetTabsContent");

            tableFilter.addEventListener("input", function () {
                const filterValue = tableFilter.value.toLowerCase();

                // Get the currently active tab

                const tabs = datasetTabsContent.querySelectorAll(".tab-pane");
                tabs.forEach(tab => {
                    const rows = tab.querySelectorAll("table tbody tr");

                    rows.forEach(row => {
                        const textContent = row.textContent.toLowerCase();
                        if (textContent.indexOf(filterValue) > -1) {
                            row.style.display = "";
                        } else {
                            row.style.display = "none";
                        }
                    });
                });
            });

        });
        // Clear the filter when switching tabs
        document.addEventListener("DOMContentLoaded", function () {
            const tableFilter = document.getElementById("tableFilter");
            const clearFilter = document.getElementById("clearFilter");

            clearFilter.addEventListener("click", function () {
                tableFilter.value = "";
                const tabs = document.getElementById("datasetTabsContent").querySelectorAll(".tab-pane");
                tabs.forEach(tab => {
                    const rows = tab.querySelectorAll("table tbody tr");
                    rows.forEach(row => {
                        row.style.display = "";
                    });
                });
            });
        });
