function sendMessageFromClient(text) { // réécrire
    html = `<div class="UserMessage card text-end border-0">
    <p class="card-title fw-bold">Vous</p>
    <div class="card-body text-break">
      `+ text + `
    </div>
  </div>`;

    $('#ChatBox').append(html);
  }

  function sendMessageFromBot(text) { // réécrires
    html = `<div class="BotMessage card border-0 lh-1">
    <p class="DisplayNames card-title fw-bold text-primary">🤖 Bot</p>
    <div class="BotMessageBody card-body text-break border border-primary border-2 rounded">
      `+ text + `
    </div>
  </div>`;

    $('#ChatBox').append(html);
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
        success: function(data){
          console.log(data);
        },
        error: function(error){
          console.log(error);
        }
      })

      return false; // Permet de ne pas recharger la page
    });

  });