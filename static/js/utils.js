function openModal(titleId, descriptionId, imageId) {
  var title = document.getElementById(titleId).innerHTML;
  var description = document.getElementById(descriptionId).innerHTML;
  var imagen = document
    .getElementById(imageId)
    .src.split("http://127.0.0.1:5500/")[1];

  var modalContent = `
  <div id="myModal" class="modal">
  <div class="modal-content">
    <div class="modal-header">
      <span class="close">&times;</span>
      <h2>${title}</h2>
    </div>

    <div class="main">
      <!-- empieza la card -->
      <div class="column" id="card">
        <img  
          class="borderRadius imgCard"
          src="${imagen}"
          alt="${imagen}"
          height="50%"
          width="60%"
        />
        <div class="description">
          <p>${description}</p>
          <div class="interaction row alignEnd">
            <!-- <span style="font-size: 50px">&#10084;</span> -->
            <!--esto no funciona porque al llamar a la fucnion change color no me esta tomando el id de la imagen <img
              style="display: block"
              id="heartImg"
              onclick="changeColor()"
              src="heart3.png"
              width="30"
              alt="corazon"
            />
            <img
              style="display: none"
              id="heartImg1"
              onclick="changeColor1()"
              src="heart2.png"
              width="30"
              alt="corazon"
            /> -->
          </div>
        </div>
      </div>
    </div>
    <!-- termina la card -->
    <!-- comentarios -->
    <div class="col commentsContainer">
      <div class="row comments">
        <div class="row">
          <div class="column">
            <img
              src="images/face1.png"
              width="50px"
              height="50px"
              class="avatar"
            />
          </div>
          <div class="column commentContent">
            <div><b>Nombre Apellido</b></div>
            <div>Welcome to the Jungle</div>
          </div>
        </div>
      </div>
      <div class="row comments">
        <div class="row">
          <div class="column">
            <img
              src="images/face2.png"
              width="50px"
              height="50px"
              class="avatar"
            />
          </div>
          <div class="column commentContent">
            <div><b>Nombre Apellido</b></div>
            <div>
              we've got fun and games
              <span style="font-size: 20px">&#128070;</span>
            </div>
          </div>
        </div>
      </div>
      <div class="row comments">
        <div class="row">
          <div class="column">
            <img
              src="images/face3.png"
              width="50px"
              height="50px"
              class="avatar"
            />
          </div>
          <div class="column commentContent">
            <div><b>Nombre Apellido</b></div>
            <div>We got everything you want honey</div>
          </div>
        </div>
      </div>
      <a class="row" href="">Ver mas comentarios</a>
      <form class="row comments" id="inputComment" autocomplete="off">
        <input
          type="text"
          name="fname"
          placeholder="Escribe un comentario..."
          style="width: 100%; height: 30px; border-radius: 8px"
        />
        <input
          type="submit"
          value="Comentar"
          style="border-radius: 8px"
          class="imputBtn"
        />
      </form>
    </div>
    <!-- comentarios -->
  </div>
</div>`;
  document.getElementById("displayContent").innerHTML = modalContent;

  // Get the modal
  var modal = document.getElementById("myModal");

  // Get the button that opens the modal
  var btn = document.getElementById("myBtn");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal
  btn.onclick = function () {
    modal.style.display = "block";
  };

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  };
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
  // function changeColor() {
  //   document.getElementById(heartImg).style.display = "none";
  //   document.getElementById(heartImg1).style.display = "block";
  // }

  // function changeColor1() {
  //   document.getElementById(heartImg).style.display = "block";
  //   document.getElementById(heartImg1).style.display = "none";
  // }
}
