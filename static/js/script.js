/*
  JS scripts managing all the functions regarding the user's and bot's answers.
  Also contains an AJAX request to send and receive data to/from Flask.
*/

function sendMessageFromClient(text) { 
  /*
    Function used to send a message from the user side.
    * Arguments:
      - text : contains the user's input.
    */
    let id = Date.now();
    $('#ChatBox').append(`<div id="`+ id +`" class="UserMessage card text-end border-0" style="background-color: #121212;color: white"></div>`);
    $('#' + id).append(`<p class="card-title fw-bold">Vous</p>`)
    $('#' + id).append(`<div class="UserMessageBody card-body text-break"></div>`)
    $('#' + id + ' .UserMessageBody').html(text)
  }

  function sendMessageFromBot(text) { // réécrires
    /*
    Function used to send a message from the bot side.
    * Arguments:
      - text : contains the bot's answer.
    */
    let id = Date.now();
    $('#ChatBox').append(`<div id="`+ id +`" class="BotMessage card border-0 lh-1" style="background-color: #121212"></div>`);
    $('#' + id).append(`<p class="DisplayNames card-title fw-bold text-primary">🤖 Bot</p>`);
    $('#' + id).append(`<div class="BotMessageBody card-body text-break border border-primary border-2 rounded"></div>`);
    $('#' + id + ' .BotMessageBody').html(text);
  }

  $(function () { // Quand la page a fini de charger
    $('#UserInputForm').on('submit', function (event) {
    /*
    Function used to execute some code once the submit button
    from the form with id UserInputForm is pressed (or enter key
    pressed).
    * Return:
      false : to prevent the page from reloading.
    */
      event.preventDefault();

      var content = $('#UserInput').val();
      $('#UserInput').val("");

      sendMessageFromClient(content);

      $.ajax({
        /*
        AJAX request made to send and receive data to/from Flask.
        */
        url : '/getuserdata',
        type : "POST",
        data: {userinput : content},
        dataType: "json",
        success: function(data){
          console.log(data);
          sendMessageFromBot(data.answer)
          initMap(data.lat, data.lng);
        },
        error: function(error){
          console.log(error);
        }
      })

      let map;
      function initMap(dlat, dlng) {
        /*
        Function used to update the interactive map on the
        application. It also updates the cursor on the map.
        * Arguments:
          - dlat : meaning "data latitude". Corresponds to the
          latitude received from the AJAX request, from Flask.
          - dlng : meaning "data longitude". Corresponds to the
          longitude received from the AJAX request, from Flask.
        */
        map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: dlat, lng: dlng },
          zoom: 8,
        });
        const marker = new google.maps.Marker({
          position: { lat: dlat, lng: dlng },
          map: map,
        });
      }
      return false;
    });

  });