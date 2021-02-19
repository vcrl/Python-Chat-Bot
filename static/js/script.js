function sendMessageFromClient(text) { 
  
    let id = Date.now();
    $('#ChatBox').append(`<div id="`+ id +`" class="UserMessage card text-end border-0"></div>`);
    $('#' + id).append(`<p class="card-title fw-bold">Vous</p>`)
    $('#' + id).append(`<div class="UserMessageBody card-body text-break"></div>`)
    $('#' + id + ' .UserMessageBody').html(text)
  }

  function sendMessageFromBot(text) { // réécrires
    
    let id = Date.now();
    $('#ChatBox').append(`<div id="`+ id +`" class="BotMessage card border-0 lh-1"></div>`);
    $('#' + id).append(`<p class="DisplayNames card-title fw-bold text-primary">🤖 Bot</p>`);
    $('#' + id).append(`<div class="BotMessageBody card-body text-break border border-primary border-2 rounded"></div>`);
    $('#' + id + ' .BotMessageBody').html(text);
  }

  $(function () { // Quand la page a fini de charger

    $('#UserInputForm').on('submit', function (event) { // Lorsque le formulaire avec l'id UserInputForm est envoyé (soit entré, soit cliquer sur le bouton)
      event.preventDefault();

      var content = $('#UserInput').val(); // Récupération des données de l'élement html avec l'id UserInput
      $('#UserInput').val(""); // Écriture de l'attribut value par une chaine de caractère vide

      sendMessageFromClient(content);

      $.ajax({
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
        map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: dlat, lng: dlng },
          zoom: 8,
        });
        const marker = new google.maps.Marker({
          position: { lat: dlat, lng: dlng },
          map: map,
        });
      }
      return false; // Permet de ne pas recharger la page
    });

  });