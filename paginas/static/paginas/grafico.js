function(){
    var url = "/grafico/";
    getJSON(url, function(res)) {
        var data = res.note.map(function (v) {
            return [v.date, v.total_cost]
        });
    }
}