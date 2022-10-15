var data_bar = [];
    data_bar.data = [158.308, 256.188, 124.118, 346.706, 234.5, 547.468];
    data_bar.labels = ['A-212', 'B-111', 'C-462', 'B-129', 'D-019', 'E-001'];
var data_radar = [];
    data_radar.data = [56, 34, 67, 98, 12, 76];
    data_radar.labels = ['Applied Optics', 'Applied Physics B: Lasers and Optics', 'Computing and Visualization in Science', 'Fiber and Integrated Optics', 'Journal of Biomedical Optics', 'Journal of Modern Optics'];
var data_bublik = [];
    data_bublik.data = [10, 20, 10, 50, 5, 5];
    data_bublik.labels = ['Optic in %', 'Laser in %', 'Maser in %', 'Theorist in %', 'Lens in %', 'Other in %'];
var data_polar = [];
    data_polar.data = [1.308, 5.188, 7.118, 2.706, 9.5, 3.468];
    data_polar.labels = ['Optic', 'Laser', 'Maser', 'Theorist', 'Lens', 'Other'];
var backgroundColor = [
    'rgba(216, 27, 96, 0.6)',
    'rgba(3, 169, 244, 0.6)',
    'rgba(255, 152, 0, 0.6)',
    'rgba(29, 233, 182, 0.6)',
    'rgba(156, 39, 176, 0.6)',
    'rgba(84, 110, 122, 0.6)'];
var borderColor = [
    'rgba(216, 27, 96, 1)',
    'rgba(3, 169, 244, 1)',
    'rgba(255, 152, 0, 1)',
    'rgba(29, 233, 182, 1)',
    'rgba(156, 39, 176, 1)',
    'rgba(84, 110, 122, 1)'];

var ctx = document.getElementById('1').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: data_bar.labels,
        datasets: [{
            labels: 'Graphic',
            data: data_bar.data,
            backgroundColor: backgroundColor,
            borderColor: borderColor,
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Graphic',
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
    type: 'radar',
    data: {
        labels: data_radar.labels,
        datasets: [{
            label: 'Journal reads',
            data: data_radar.data,
            backgroundColor: backgroundColor,
            borderColor: borderColor,
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Graphic',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
    }
});

var ctx = document.getElementById('3').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: data_bublik.labels,
        datasets: [{
            label: 'Graphic',
            data: data_bublik.data,
            backgroundColor: backgroundColor,
            borderColor: borderColor,
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Graphic',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
    }
});

var ctx = document.getElementById('4').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'polarArea',
    data: {
        labels: data_polar.labels,
        datasets: [{
            label: 'Graphic',
            data: data_polar.data,
            backgroundColor: backgroundColor,
            borderColor: borderColor,
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Graphic',
            position: 'top',
            fontSize: 16,
            padding: 20
        },
    }
});
