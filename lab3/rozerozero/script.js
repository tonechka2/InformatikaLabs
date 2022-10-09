var ctx = document.getElementById('1').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Hong Kong', 'Macau', 'Japan', 'Switzerland', 'Spain', 'Singapore'],
        datasets: [{
            label: 'Life expectancy',
            data: [84.308, 84.188, 84.118, 83.706, 83.5, 83.468],
            backgroundColor: [
                'rgba(216, 27, 96, 0.6)',
                'rgba(3, 169, 244, 0.6)',
                'rgba(255, 152, 0, 0.6)',
                'rgba(29, 233, 182, 0.6)',
                'rgba(156, 39, 176, 0.6)',
                'rgba(84, 110, 122, 0.6)'
            ],
            borderColor: [
                'rgba(216, 27, 96, 1)',
                'rgba(3, 169, 244, 1)',
                'rgba(255, 152, 0, 1)',
                'rgba(29, 233, 182, 1)',
                'rgba(156, 39, 176, 1)',
                'rgba(84, 110, 122, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Life Expectancy by Country',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
        scales: {
            yAxes: [{
                ticks: {
                    min: 75
                }
            }]
        }
    }
});

var ctx = document.getElementById('2').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'polarArea',
    data: {
        labels: ['Hong Kong', 'Macau', 'Japan', 'Switzerland', 'Spain', 'Singapore'],
        datasets: [{
            label: 'Life expectancy',
            data: [84.308, 84.188, 84.118, 83.706, 83.5, 83.468],
            backgroundColor: [
                'rgba(216, 27, 96, 0.6)',
                'rgba(3, 169, 244, 0.6)',
                'rgba(255, 152, 0, 0.6)',
                'rgba(29, 233, 182, 0.6)',
                'rgba(156, 39, 176, 0.6)',
                'rgba(84, 110, 122, 0.6)'
            ],
            borderColor: [
                'rgba(216, 27, 96, 1)',
                'rgba(3, 169, 244, 1)',
                'rgba(255, 152, 0, 1)',
                'rgba(29, 233, 182, 1)',
                'rgba(156, 39, 176, 1)',
                'rgba(84, 110, 122, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Life Expectancy by Country',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
        scales: {
            yAxes: [{
                ticks: {
                    min: 75
                }
            }]
        }
    }
});

var ctx = document.getElementById('3').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Hong Kong', 'Macau', 'Japan', 'Switzerland', 'Spain', 'Singapore'],
        datasets: [{
            label: 'Life expectancy',
            data: [84.308, 84.188, 84.118, 83.706, 83.5, 83.468],
            backgroundColor: [
                'rgba(216, 27, 96, 0.6)',
                'rgba(3, 169, 244, 0.6)',
                'rgba(255, 152, 0, 0.6)',
                'rgba(29, 233, 182, 0.6)',
                'rgba(156, 39, 176, 0.6)',
                'rgba(84, 110, 122, 0.6)'
            ],
            borderColor: [
                'rgba(216, 27, 96, 1)',
                'rgba(3, 169, 244, 1)',
                'rgba(255, 152, 0, 1)',
                'rgba(29, 233, 182, 1)',
                'rgba(156, 39, 176, 1)',
                'rgba(84, 110, 122, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Life Expectancy by Country',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
        scales: {
            yAxes: [{
                ticks: {
                    min: 75
                }
            }]
        }
    }
});

var ctx = document.getElementById('4').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ['Hong Kong', 'Macau', 'Japan', 'Switzerland', 'Spain', 'Singapore'],
        datasets: [{
            label: 'Life expectancy',
            data: [84.308, 84.188, 84.118, 83.706, 83.5, 83.468],
            backgroundColor: [
                'rgba(216, 27, 96, 0.6)',
                'rgba(3, 169, 244, 0.6)',
                'rgba(255, 152, 0, 0.6)',
                'rgba(29, 233, 182, 0.6)',
                'rgba(156, 39, 176, 0.6)',
                'rgba(84, 110, 122, 0.6)'
            ],
            borderColor: [
                'rgba(216, 27, 96, 1)',
                'rgba(3, 169, 244, 1)',
                'rgba(255, 152, 0, 1)',
                'rgba(29, 233, 182, 1)',
                'rgba(156, 39, 176, 1)',
                'rgba(84, 110, 122, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Life Expectancy by Country',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
        scales: {
            yAxes: [{
                ticks: {
                    min: 75
                }
            }]
        }
    }
});
