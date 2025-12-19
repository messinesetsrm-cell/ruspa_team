import streamlit as st
import streamlit.components.v1 as components

# Configurazione pagina
st.set_page_config(page_title="Verifica Nome", page_icon="🕵️‍♂️")

st.title("Verifica il tuo profilo")

# Input dell'utente
nome_input = st.text_input("Inserisci il tuo nome:")

# Lista dei nomi "speciali"
nomi_target = ["pierluigi", "pierluigi de rubeis", "ruspa", "de rubeis", "pier"]

if nome_input:
    nome_pulito = nome_input.strip().lower()

    if nome_pulito in nomi_target:
        st.subheader(f"Sei un pagliaccio, {nome_input}! 🤡")
        
        # --- INIZIO CODICE GIOCO CON TIMER ---
        st.write("### 🧹 MINIGIOCO: Hai 30 secondi!")
        
        game_html = """
        <div id="game-container" style="text-align: center; font-family: Arial, sans-serif;">
            <div id="ui-layer">
                <span id="timer" style="font-size: 24px; color: red; font-weight: bold;">Tempo: 30</span>
                <span id="scoreBoard" style="font-size: 24px; margin-left: 20px;">Punti: 0</span>
            </div>
            <canvas id="gameCanvas" width="400" height="300" style="border:2px solid #000; background: #f0f8ff; cursor: none; margin-top: 10px;"></canvas>
            <div id="final-screen" style="display: none; padding: 20px;">
                <h2>⏰ TEMPO SCADUTO!</h2>
                <p id="final-score" style="font-size: 20px;"></p>
                <button onclick="resetGame()" style="padding: 10px; cursor: pointer;">Gioca Ancora</button>
            </div>
        </div>

        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            const scoreBoard = document.getElementById("scoreBoard");
            const timerDisplay = document.getElementById("timer");
            const finalScreen = document.getElementById("final-screen");
            const finalScoreTxt = document.getElementById("final-score");

            let score = 0;
            let timeLeft = 30;
            let gameActive = true;
            let clown = { x: 200, y: 150, size: 40 };
            let broom = { x: Math.random() * 350, y: Math.random() * 250, size: 35 };

            // Timer
            const countdown = setInterval(() => {
                if (gameActive) {
                    timeLeft--;
                    timerDisplay.innerHTML = "Tempo: " + timeLeft;
                    if (timeLeft <= 0) {
                        endGame();
                    }
                }
            }, 1000);

            canvas.addEventListener("mousemove", (e) => {
                if (!gameActive) return;
                const rect = canvas.getBoundingClientRect();
                clown.x = e.clientX - rect.left - clown.size / 2;
                clown.y = e.clientY - rect.top - clown.size / 2;
            });

            function endGame() {
                gameActive = false;
                canvas.style.display = "none";
                document.getElementById("ui-layer").style.display = "none";
                finalScreen.style.display = "block";
                finalScoreTxt.innerHTML = "Hai preso " + score + " scope! 🧹";
            }

            function resetGame() {
                score = 0;
                timeLeft = 30;
                gameActive = true;
                canvas.style.display = "block";
                document.getElementById("ui-layer").style.display = "block";
                finalScreen.style.display = "none";
                scoreBoard.innerHTML = "Punti: 0";
                timerDisplay.innerHTML = "Tempo: 30";
            }

            function draw() {
                if (gameActive) {
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    ctx.font = "40px Arial";
                    ctx.fillText("🤡", clown.x, clown.y + 30);
                    ctx.fillText("🧹", broom.x, broom.y + 30);

                    // Collisione
                    if (clown.x < broom.x + 30 && clown.x + 30 > broom.x &&
                        clown.y < broom.y + 30 && clown.y + 30 > broom.y) {
                        score++;
                        scoreBoard.innerHTML = "Punti: " + score;
                        broom.x = Math.random() * 350;
                        broom.y = Math.random() * 250;
                    }
                }
                requestAnimationFrame(draw);
            }
            draw();
        </script>
        """
        components.html(game_html, height=450)
        # --- FINE CODICE GIOCO ---

        # Questa immagine sarà sempre visibile sotto il gioco, 
        # oppure puoi caricarla solo alla fine se preferisci.
        st.image("rsupa2.jpeg", caption="Momento celebrazione!", width=400)
        st.image("pagliaccio.jpg", caption="Il pagliaccio originale", width=400)

    else:
        st.subheader(f"Sei un grande, {nome_input}!")
        st.image("https://img.freepik.com/free-vector/golden-trophy-cup_1284-4733.jpg",
                 caption="Il campione!", width=400)
