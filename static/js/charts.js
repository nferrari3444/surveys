function pollResultsData(data) {


    
    console.log('dataaaaa', data)

    const data_ = data['pollInfo']

    const question = data['question']
    const choices = []
    const values = []

    data_.map((item => choices.push(item['selectedchoice'])))

    data_.map((item => values.push(item['votes'])))

    console.log('choices', choices)

    console.log('values', values)

    console.log(choices[0])
    console.log(choices[1])

    document.querySelector(".modal-fader").className += " active";
    document.querySelector('#myModal').className += " active";
   
    var closemodal = document.querySelector(".modal-off")
    console.log(closemodal)
    
    var modalWindow = document.querySelector(".modal-window");
    var modalFader = document.querySelector(".modal-fader");
    
    document.querySelector(".modal-off").addEventListener('click', function () {
      
          console.log('hola hola')
            modalFader.className = modalFader.className.replace("active", "");
        
            modalWindow.className = modalWindow.className.replace("active", "");
      
          })

    var chartContainer = document.getElementById("chartContainer");
    
    var chart = new CanvasJS.Chart(chartContainer, {



        exportEnabled: false,
        animationEnabled: true,
        title:{
            text: question
        },
        subtitles: [{
            text: ""
        }], 
        axisX: {
            title: "Choices"
        },
        axisY: {
            title: "Votes",
            titleFontColor: "#4F81BC",
            lineColor: "#4F81BC",
            labelFontColor: "#4F81BC",
            tickColor: "#4F81BC",
            includeZero: true
        },
      
        toolTip: {
            shared: true
        },
        legend: {
            cursor: "pointer",
           // itemclick: toggleDataSeries
        },
        data: [{
            type: "column",
            name: "Votes",
            showInLegend: true,      
            yValueFormatString: "#,##0.#",
            
             dataPoints: [
                 { label: choices[0], y: values[0] }, 
                 { label: choices[1] , y: values[1] }, 
                 { label: choices[2] , y: values[2] }, 
                

             ]
        }],
        
        
     }) ;
    chart.render();

}


