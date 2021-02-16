

      //       String URL     Object Donnes à envoyer     Fonction de retour
      $.post('./reponse.json', { contenu: content }, function (donneesRecues) {

        if (donneesRecues.etat === true) {
          sendMessageFromBot(donneesRecues.message);
        } else {
          sendMessageFromBot(donneesRecues.message || "Erreur inconnue");
        }

        // Formattage
      }, 'json');