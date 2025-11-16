import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------------
# GLOBAL PAGE CONFIG
# --------------------------------------------------------
st.set_page_config(
    page_title="Mark Chweya | Portfolio",
    page_icon="✨",
    layout="wide",
)

# --------------------------------------------------------
# REMOVE STREAMLIT DEFAULT UI (DEPLOY, MENUS, FOOTER)
# --------------------------------------------------------
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    [data-testid="stSidebar"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --------------------------------------------------------
# SESSION STATE: ACTIVE PANEL
# --------------------------------------------------------
if "panel" not in st.session_state:
    st.session_state.panel = "Home"

def switch_panel(p):
    st.session_state.panel = p

# --------------------------------------------------------
# NAVIGATION BAR
# --------------------------------------------------------
navbar_css = """
<style>
.navbar {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255,255,255,0.06);
    padding: 12px 40px;
    border-radius: 16px;
    box-shadow: 0 0 25px rgba(255,215,0,0.35);
    backdrop-filter: blur(20px);
    z-index: 9999;
}
.nav-item {
    padding: 0 22px;
    font-size: 20px;
    font-weight: 600;
    color: #f5d97c;
    cursor: pointer;
    text-decoration: none;
}
.nav-item:hover {
    text-shadow: 0 0 10px gold;
}
</style>
"""
st.markdown(navbar_css, unsafe_allow_html=True)

navbar_html = f"""
<div class='navbar'>
    <span class='nav-item' onclick="sendPanel('Home')">Home</span>
    <span class='nav-item' onclick="sendPanel('Projects')">Projects</span>
    <span class='nav-item' onclick="sendPanel('About')">About</span>
    <span class='nav-item' onclick="sendPanel('Resume')">Resume</span>
    <span class='nav-item' onclick="sendPanel('Contact')">Contact</span>
</div>

<script>
function sendPanel(panel) {{
    window.parent.postMessage({{"panel": panel}}, "*");
}}
</script>
"""

components.html(navbar_html, height=70)
# --------------------------------------------------------
# HERO SECTION (FULLSCREEN, NO SCROLL)
# --------------------------------------------------------
hero_html = """
<style>

body, html {
    overflow: hidden !important;  /* No scrolling */
    height: 100vh;
    width: 100vw;
}

/* Fullscreen hero container */
.hero-wrap {
    position: relative;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
}

/* Text (left side) */
.hero-text {
    position: absolute;
    top: 50%;
    left: 6%;
    transform: translateY(-50%);
    z-index: 20;
}

.hero-name {
    font-size: 56px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
}

.hero-role {
    font-size: 24px;
    opacity: 0.85;
    margin-top: -8px;
    color: #e5e5e5;
}

/* Avatar canvas (RIGHT side) */
#avatarCanvas {
    position: absolute;
    right: 4%;
    top: 50%;
    transform: translateY(-50%);
    width: 32%;
    height: 70%;
    z-index: 15;
}

/* Gold rings */
#ringsCanvas {
    position:absolute;
    left:0;
    top:0;
    width:100%;
    height:100%;
    z-index: 5;
}

/* Rising Adinkra symbols */
#adinkraCanvas {
    position:absolute;
    left:0;
    top:0;
    width:100%;
    height:100%;
    z-index: 4;
}

/* BLUR BACKGROUND WHEN PANEL OPENS */
.blur-bg {
    filter: blur(12px) brightness(0.45);
    transition: 0.3s ease;
}

.unblur-bg {
    filter: none;
    transition: 0.3s ease;
}

</style>


<div class="hero-wrap" id="hero">

    <!-- Rising Adinkra -->
    <canvas id="adinkraCanvas"></canvas>

    <!-- Rotating rings -->
    <canvas id="ringsCanvas"></canvas>

    <!-- Avatar -->
    <canvas id="avatarCanvas"></canvas>

    <!-- Text -->
    <div class="hero-text">
        <div class="hero-name">Mark Chweya</div>
        <div class="hero-role">Data Science & Artificial Intelligence</div>
    </div>

</div>


<!-- LOAD THREE.JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>


<script>

// =============================================================
// CANVAS HELPERS
// =============================================================
function fitCanvas(c){
    const w = c.clientWidth, h = c.clientHeight;
    if(c.width != w || c.height != h){
        c.width = w;
        c.height = h;
    }
}

// =============================================================
// RISING ADINKRA SYMBOLS (LIGHT MODE)
// =============================================================
const aCanvas = document.getElementById("adinkraCanvas");
const actx = aCanvas.getContext("2d");
const symbols = ["✺","✤","❂"];
let adinkra = [];

function initAdinkra(){
    fitCanvas(aCanvas);
    adinkra = [];
    for(let i=0;i<20;i++){
        adinkra.push({
            x: Math.random()*aCanvas.width,
            y: Math.random()*aCanvas.height,
            size: 12 + Math.random()*8,
            speed: 0.4 + Math.random()*0.5,
            char: symbols[Math.floor(Math.random()*symbols.length)]
        });
    }
}

function animateAdinkra(){
    fitCanvas(aCanvas);
    actx.clearRect(0,0,aCanvas.width,aCanvas.height);
    actx.fillStyle = "rgba(255,215,0,0.85)";

    adinkra.forEach(s=>{
        actx.font = s.size+"px serif";
        actx.fillText(s.char, s.x, s.y);
        s.y -= s.speed;
        if(s.y < -20){
            s.y = aCanvas.height + 20;
            s.x = Math.random()*aCanvas.width;
        }
    });

    requestAnimationFrame(animateAdinkra);
}

initAdinkra();
animateAdinkra();


// =============================================================
// GOLD ROTATING RINGS
// =============================================================
const rCanvas = document.getElementById("ringsCanvas");
const rctx = rCanvas.getContext("2d");

function animateRings(){
    fitCanvas(rCanvas);
    const w = rCanvas.width, h = rCanvas.height;

    rctx.clearRect(0,0,w,h);

    const cx = w * 0.70;  // shift to right (behind avatar)
    const cy = h * 0.50;
    const t = Date.now() * 0.00004;

    for(let i=0;i<3;i++){
        const R = 120 + i*35;

        rctx.beginPath();
        rctx.arc(cx, cy, R, 0, Math.PI*2);
        rctx.strokeStyle = "rgba(255,215,0,"+(0.45-i*0.1)+")";
        rctx.lineWidth = 3;

        rctx.save();
        rctx.translate(cx,cy);
        rctx.rotate((i%2===0 ? 1 : -1) * t);
        rctx.translate(-cx,-cy);
        rctx.stroke();
        rctx.restore();
    }

    requestAnimationFrame(animateRings);
}
animateRings();


// =============================================================
// 3D AVATAR
// =============================================================
const avatarCanvas = document.getElementById("avatarCanvas");
const renderer = new THREE.WebGLRenderer({canvas: avatarCanvas, alpha:true});
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
camera.position.set(0,1.1,2.4);

const key = new THREE.DirectionalLight(0xf6d47a,1.2);
key.position.set(2,3,4);
scene.add(key);

const fill = new THREE.DirectionalLight(0xffffff,0.4);
fill.position.set(-2,0,3);
scene.add(fill);

let avatar = null;

const loader = new THREE.GLTFLoader();
loader.load(
    "https://models.readyplayer.me/691a321f28f4be8b0c02cf2e.glb",
    gltf=>{
        avatar = gltf.scene;
        avatar.scale.set(1.55,1.55,1.55);
        avatar.position.y = -1.28;
        scene.add(avatar);
    }
);

let dragging=false, prevX=0, rot=0.004;

avatarCanvas.addEventListener("mousedown", e=>{
    dragging=true; prevX=e.clientX;
});
window.addEventListener("mouseup", ()=>dragging=false);
window.addEventListener("mousemove", e=>{
    if(dragging && avatar){
        rot = (e.clientX - prevX)*0.0004;
        prevX = e.clientX;
    }
});

function animateAvatar(){
    requestAnimationFrame(animateAvatar);
    if(avatar) avatar.rotation.y += rot;
    renderer.setSize(avatarCanvas.clientWidth, avatarCanvas.clientHeight);
    renderer.render(scene,camera);
}
animateAvatar();


// =============================================================
// PANEL OPEN/CLOSE BLUR CONTROL
// (Executed from Part 3)
// =============================================================
window.addEventListener("message", (event)=>{
    if(event.data.blur){
        document.getElementById("hero").classList.add("blur-bg");
    } else {
        document.getElementById("hero").classList.remove("blur-bg");
    }
});

</script>
"""

components.html(hero_html, height=850)
# --------------------------------------------------------
# SLIDING PANEL SYSTEM (Smooth horizontal transitions)
# --------------------------------------------------------
panel_engine = """
<style>

.panel-container {
    position: fixed;
    top: 0;
    left: 100vw;              /* Start off-screen on the RIGHT */
    width: 100vw;
    height: 100vh;
    background: rgba(10,10,10,0.75);
    backdrop-filter: blur(18px);
    transition: all 0.30s ease;   /* SMOOTH */
    z-index: 9998;
    padding: 120px 80px;
    color: #f5f5f5;
    overflow: hidden;
}

/* When panel is active (slide into view) */
.panel-active {
    left: 0 !important;
}

/* Close button */
.close-btn {
    position: absolute;
    top: 30px;
    right: 40px;
    font-size: 32px;
    cursor: pointer;
    color: #f6d47a;
}
.close-btn:hover {
    text-shadow: 0 0 12px gold;
}

.panel-title {
    font-size: 48px;
    font-weight: 900;
    margin-bottom: 25px;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
}

.panel-content {
    font-size: 20px;
    line-height: 1.55;
    width: 60%;
}

</style>

<div id="slidePanel" class="panel-container">
    <div class="close-btn" onclick="closePanel()">×</div>
    <div id="panelInner"></div>
</div>

<script>

/* COMMUNICATION BETWEEN STREAMLIT + JS */
window.addEventListener("message", (event) => {
    if (event.data.type === "open-panel") {
        openPanel(event.data.content);
    }
    if (event.data.type === "close-panel") {
        closePanel();
    }
});

/* OPEN PANEL */
function openPanel(htmlContent) {
    const panel = document.getElementById("slidePanel");
    document.getElementById("panelInner").innerHTML = htmlContent;

    panel.classList.add("panel-active");

    window.parent.postMessage({ "blur": true }, "*");
}

/* CLOSE PANEL */
function closePanel() {
    const panel = document.getElementById("slidePanel");
    panel.classList.remove("panel-active");

    window.parent.postMessage({ "blur": false }, "*");
}

</script>
"""

components.html(panel_engine, height=0)
# --------------------------------------------------------
# PANEL CONTENT DEFINITIONS (HTML)
# --------------------------------------------------------

def make_html_panel(title, body):
    return f"""
    <div class='panel-title'>{title}</div>
    <div class='panel-content'>{body}</div>
    """

# ---------- PROJECTS PANEL ----------
projects_html = make_html_panel(
    "Projects",
    """
    <p><b>🔹 Titanic Survival Predictor</b><br>
    Machine learning model predicting Titanic survival.<br>
    <a href='https://markchweya.shinyapps.io/Titanic-Survival-Rate-Predictor/' target='_blank' style='color:#f6d47a;'>Open Project →</a></p>

    <p><b>🔹 AQI Predictor</b><br>
    Predicting Air Quality Index using ML.<br>
    <a href='https://aqi-predictor2.streamlit.app' target='_blank' style='color:#f6d47a;'>Open App →</a></p>

    <p><b>🔹 Mental Health Predictor (USA)</b><br>
    Predict likelihood of needing mental health treatment.<br>
    <a href='https://mentalhealthpredictorusa.streamlit.app' target='_blank' style='color:#f6d47a;'>Open Predictor →</a></p>

    <p><b>🔹 KukiLabs</b><br>
    A collection of AI tools, experiments and prototypes.<br>
    <a href='https://kukilabs.streamlit.app' target='_blank' style='color:#f6d47a;'>Explore KukiLabs →</a></p>
    """
)

# ---------- ABOUT PANEL ----------
about_html = make_html_panel(
    "About Me",
    """
    I am <b>Mark Chweya</b>, a Data Science & Analytics student at USIU–Africa.<br><br>

    My work blends:<br>
    • Machine Learning<br>
    • Predictive Modeling<br>
    • Data Visualization<br>
    • Artificial Intelligence<br>
    • Creative futuristic UI design<br><br>

    I specialize in building interactive AI tools with a unique African futurist identity.
    """
)

# ---------- RESUME PANEL ----------
resume_html = make_html_panel(
    "Resume",
    """
    <b>🎓 Education</b><br>
    • USIU–Africa — BSc. Applied Computer Technology (Data Science & Analytics)<br>
    • Moringa School — Software Engineering<br>
    • Pioneer School — KCSE<br><br>

    <b>🛠 Skills</b><br>
    Python, R, SQL, Machine Learning<br>
    Streamlit, React, Data Visualization<br>
    Predictive Modelling, AI Systems<br><br>

    <b>🏅 Certifications</b><br>
    • Certificate in Computer Programming<br><br>

    <b>🏀 Interests</b><br>
    • Football (Manchester United)<br>
    • Basketball (Lakers)<br>
    • Golf<br>
    • AI research and UI/UX futurism<br><br>

    <b>📞 Contact</b><br>
    Email: <span style='color:#f6d47a;'>chweyamark@gmail.com</span><br>
    Phone: <span style='color:#f6d47a;'>+254 703 951 840</span>
    """
)

# ---------- CONTACT PANEL ----------
contact_html = make_html_panel(
    "Contact Me",
    """
    Want to collaborate, hire me, or discuss a project?<br><br>

    <b>Email:</b> <span style='color:#f6d47a;'>chweyamark@gmail.com</span><br>
    <b>Phone:</b> <span style='color:#f6d47a;'>+254 703 951 840</span><br><br>

    <b>Message Form (future integration):</b><br><br>
    <i>This will be replaced with a live email-sending backend.</i>
    """
)

# --------------------------------------------------------
# MAP PANEL NAMES → HTML CONTENT
# --------------------------------------------------------
panel_mapping = {
    "Projects": projects_html,
    "About": about_html,
    "Resume": resume_html,
    "Contact": contact_html
}
# --------------------------------------------------------
# PART 5 — FINAL PANEL TRIGGER LOGIC
# --------------------------------------------------------

# Listen for navbar click events via postMessage
components.html(
    """
    <script>
    window.addEventListener("message", (event) => {
        if (event.data.panel) {
            window.parent.postMessage({"set-panel": event.data.panel}, "*");
        }
    });
    </script>
    """,
    height=0
)

# Handle message from JS (navbar → python)
def handle_panel_message():
    msg = st.experimental_get_query_params()  # Only used for updates
    # But actual panel switching will be done via JS → Streamlit bridge below


# --------------------------------------------------------
# JS BRIDGE: NAVBAR → STREAMLIT SESSION STATE
# --------------------------------------------------------
bridge = """
<script>
window.addEventListener("message", (event) => {
    if (event.data["set-panel"]) {
        const p = event.data["set-panel"];
        fetch("/?panel=" + p)  // triggers rerun with correct panel
    }
});
</script>
"""
components.html(bridge, height=0)

# Read panel param (set by JS bridge)
if "panel" in st.query_params:
    st.session_state.panel = st.query_params["panel"]


# --------------------------------------------------------
# OPEN OR CLOSE PANELS BASED ON STATE
# --------------------------------------------------------

if st.session_state.panel != "Home":
    # Send command to JS panel engine
    components.html(
        f"""
        <script>
        window.parent.postMessage({{
            type: "open-panel",
            content: `{panel_mapping[st.session_state.panel]}`
        }}, "*");
        </script>
        """,
        height=0
    )

else:
    # Close any open panels
    components.html(
        """
        <script>
        window.parent.postMessage({ type: "close-panel" }, "*");
        </script>
        """,
        height=0
    )
