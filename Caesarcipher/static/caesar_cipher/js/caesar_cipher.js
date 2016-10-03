$(document).ready(function () {
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    var csrftoken = $.cookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //different colors  for bar
    function getRandomColor(let) {
        var colors =[];
        var x=0;
        while ( x < let.length ) {
                color ='#'+Math.random().toString(16).substr(-6);
                colors.push(color)
            x++;
        }
        return colors;
    }

    //drawing bar
    function diagramm(data){
    var ctx = $("#myChart");
    var canvas = document.getElementById("myChart").getContext("2d");

        var dat = {
           labels: data.count_let,
            datasets: [
                             {
                                        label: "Frequance of letters",
                                        backgroundColor: getRandomColor(data.count_let),
                                        borderColor: "rgb(0,0,0)",
                                        borderWidth: 1,
                                        data: data.count_f
                              }
                       ]
                    };

         var myBarChart = new Chart(ctx, {
                    type: 'bar',
                    data: dat,
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        scales: {
                                xAxes: [{
                                    stacked: false
                                }],
                                yAxes: [{
                                    stacked: true
                                }]
                        }
                    }
         });
    }

    $('#encrypt_text').on('click', function(){

        var json_data = JSON.stringify({ text_for_encrypt: $('#cipher_input').val(),
         rotation: $('#rotation_fo_action option:selected').val()});
            $.post($('#encrypt_text_u').val(), json_data, function(data){
                $('#cipher_output').val(data.ciphered_text);
                diagramm(data);
            }, 'json')

    });

    $('#decrypt_text').on('click', function(){

        var json_data = JSON.stringify({ text_for_decrypt: $('#cipher_input').val(),
         rotation: $('#rotation_fo_action option:selected').val()});
            $.post($('#decrypt_text_u').val(), json_data, function(data){
                $('#cipher_output').val(data.ciphered_text)
                  diagramm(data)
                console.log(data.count_let)
            }, 'json')
    });

    $('#brute').on('click', function(){
        var json_data = JSON.stringify({ brute_text: $('#cipher_input').val()});
            $.post($('#brute_u').val(), json_data, function(data){
                $('#cipher_output').val(data.bruted)
                  diagramm(data)

            }, 'json')
    });

    $('#detect_rot').on('click', function () {
        var json_data = JSON.stringify({ detected_num : $('#cipher_input').val()});
        $.post($('#detect_rot_u').val(),json_data, function (data) {
            var x = document.getElementById("rot");
            x.innerHTML = 'By calculating using our  newest methods, we decide that rotation is : ' + data.detect_num;

        },'json')


    })




});