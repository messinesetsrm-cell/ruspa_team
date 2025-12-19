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
        
        # --- INIZIO CODICE GIOCO ---
        st.write("### 🧹 MINIGIOCO: Prendi la ramazza!")
        st.info("Usa il MOUSE per muovere il pagliaccio e toccare la ramazza!")

        # Codice JavaScript per il gioco (funziona direttamente nel browser)
        game_html = """
        <div style="text-align: center;">
            <canvas id="gameCanvas" width="400" height="300" style="border:2px solid #000; background: #f0f8ff; cursor: none;"></canvas>
            <h2 id="scoreBoard">Punti: 0</h2>
            <button onclick="resetGame()" style="padding: 10px;">Ricomincia</button>
        </div>

        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            const scoreBoard = document.getElementById("scoreBoard");

            let score = 0;
            let clown = { x: 200, y: 150, size: 40 };
            let broom = { x: Math.random() * 350, y: Math.random() * 250, size: 35 };

            // Segue il mouse
            canvas.addEventListener("mousemove", (e) => {
                const rect = canvas.getBoundingClientRect();
                clown.x = e.clientX - rect.left - clown.size / 2;
                clown.y = e.clientY - rect.top - clown.size / 2;
            });

            function resetGame() { score = 0; scoreBoard.innerHTML = "Punti: 0"; }

            function update() {
                // Collisione semplice
                if (clown.x < broom.x + broom.size && clown.x + clown.size > broom.x &&
                    clown.y < broom.y + broom.size && clown.y + clown.size > broom.y) {
                    score++;
                    scoreBoard.innerHTML = "Punti: " + score;
                    broom.x = Math.random() * (canvas.width - 40);
                    broom.y = Math.random() * (canvas.height - 40);
                }
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Disegna Emoji
                ctx.font = "40px Arial";
                ctx.fillText("🤡", clown.x, clown.y + 30);
                ctx.fillText("🧹", broom.x, broom.y + 30);
                
                update();
                requestAnimationFrame(draw);
            }
            draw();
        </script>
        """
        # Inserisce il gioco nella pagina Streamlit
        components.html(game_html, height=450)
        # --- FINE CODICE GIOCO ---

        st.image("pagliaccio.jpg", caption="Il pagliaccio con la ramazza", width=400)
    else:
        st.subheader(f"Sei un grande, {nome_input}!")
        st.image("https://img.freepik.com/free-vector/golden-trophy-cup_1284-4733.jpg",
                 caption="Il campione!", width=400)
