const request = new Request('http://localhost:8000/api/grafico');

fetch(request).then(function(response) {
  var dados = JSON.parse(this.response);
  console.log(dados)
  var data = dados.vendas.map(function (v) {
    return [v.dia, v.valor]
  })
})

        $('#vendas').highcharts({
            chart: {
                type: 'line'
            },
            title: {
                text: 'Vendas diarias'
            },
            xAxis: {
                type: 'category'
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Valor'
                },
                plotOptions: {
                    line: {
                        dataLabels: {
                            enabled: true
                        },
                    }
                },
            },
            legend: {
                enabled: false
            },
            series: [{
                data: data,
                dataLabels: {
                    enabled: true,
                    align: 'center',
                    style: {
                        fontSize: '15px'
                    }
                }
            }],
        });
    });
});