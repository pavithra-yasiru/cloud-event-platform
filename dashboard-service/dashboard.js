const API = {
    ANALYTICS: "http://13.233.81.248:30085"
};

fetch(`${API.ANALYTICS}/analytics`)
.then(response => response.json())
.then(data => {

    let home = 0;
    let program = 0;
    let registration = 0;

    data.forEach(item => {

        if (item.event_type === "Homepage Visit")
            home++;

        if (item.event_type === "Programs Viewed")
            program++;

        if (item.event_type === "Registration Submitted")
            registration++;

    });

    // KPI Cards
    document.getElementById("homeVisits").innerHTML = home;
    document.getElementById("programViews").innerHTML = program;
    document.getElementById("registrations").innerHTML = registration;
    document.getElementById("totalEvents").innerHTML = data.length;

    // Chart
    const ctx = document.getElementById("analyticsChart");

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: [
                "Homepage Visits",
                "Program Views",
                "Registrations"
            ],

            datasets: [{

                label: "Analytics Events",

                data: [
                    home,
                    program,
                    registration
                ],

                borderWidth: 1

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    ticks: {

                        precision: 0

                    }

                }

            }

        }

    });

    // Recent Events Table
    const table = document.getElementById("analyticsTable");

    data
        .slice()
        .reverse()
        .slice(0, 10)
        .forEach(item => {

            const row = `
                <tr>
                    <td>${item.event_time}</td>
                    <td>${item.event_type}</td>
                    <td>${item.page}</td>
                </tr>
            `;

            table.innerHTML += row;

        });

})
.catch(error => {

    console.error(error);

    alert("Unable to load analytics.");

});
