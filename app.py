import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------
st.set_page_config(
    page_title="Mark Chweya | Portfolio",
    page_icon="✨",
    layout="wide"
)

# --------------------------------------------------------
# GLOBAL CSS – REMOVE STREAMLIT PADDING + SCROLLBAR
# --------------------------------------------------------
st.markdown(
    """
<style>
/* Hide default Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

/* Remove padding from the main app area */
[data-testid="stAppViewContainer"] {
    padding: 0 !important;
}

.main, .block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

/* Kill page scrolling completely */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    background: #0d0f13 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------------
# HERO SECTION — NAVBAR + NAME + AVATAR
# --------------------------------------------------------
hero_html = """
<style>
/* Reset inside iframe */
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background: #0d0f13;
    overflow: hidden;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* FULLSCREEN HERO INSIDE IFRAME (fills the iframe height) */
.hero-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 100%;
    background: #0d0f13;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    overflow: hidden;
}

/* NAVBAR */
.navbar {
    margin-top: 20px;
    display: flex;
    gap: 40px;
    padding: 10px 40px;
    background: rgba(25,25,25,0.55);
    border: 1px solid rgba(255,215,0,0.4);
    border-radius: 18px;
    backdrop-filter: blur(18px);
    z-index: 20;
}

.nav-item {
    font-size: 20px;
    font-weight: 600;
    color: #f6d47a;
    cursor: pointer;
}
.nav-item:hover {
    color: #ffffff;
    text-shadow: 0 0 10px gold;
}

/* MAIN CONTENT ROW */
.center-row {
    flex: 1;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 140px;
    /* small lift to visually center, but not so much that it causes overflow */
    transform: translateY(-10px);
}

/* LEFT — NAME */
.hero-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.hero-name {
    font-size: 70px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
}
.hero-role {
    font-size: 28px;
    color: #eaeaea;
    margin-top: -12px;
}

/* RIGHT — AVATAR */
#avatarCanvas {
    width: 380px;
    height: 520px;
    z-index: 5;
}

/* BACKGROUND CANVASES */
#ringsCanvas, #adinkraCanvas {
    position: absolute;
    left: 0; 
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
}
</style>

<div class="hero-wrap">

    <!-- NAVBAR -->
    <div class="navbar">
        <span class="nav-item" onclick="sendPanel('Home')">Home</span>
        <span class="nav-item" onclick="sendPanel('Projects')">Projects</span>
        <span class="nav-item" onclick="sendPanel('About')">About</span>
        <span class="nav-item" onclick="sendPanel('Resume')">Resume</span>
        <span class="nav-item" onclick="sendPanel('Contact')">Contact</span>
    </div>

    <!-- BACKGROUND ANIMATIONS -->
    <canvas id="adinkraCanvas"></canvas>
    <canvas id="ringsCanvas"></canvas>

    <!-- CENTERED CONTENT -->
    <div class="center-row">

        <!-- NAME -->
        <div class="hero-text">
            <div class="hero-name">Mark Chweya</div>
            <div class="hero-role">Data Science & Artificial Intelligence</div>
        </div>

        <!-- AVATAR -->
        <canvas id="avatarCanvas"></canvas>
    </div>

</div>

<!-- THREE.JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>

<script>
function fitCanvas(c){
    const w = c.clientWidth, h = c.clientHeight;
    if (c.width !== w || c.height !== h) {
        c.width = w;
        c.height = h;
    }
}

/* ADINKRA */
const aCanvas = document.getElementById("adinkraCanvas");
const actx = aCanvas.getContext("2d");
const symbols = ["✺","✤","❂"];
let adinkra = [];

function initAdinkra(){
    fitCanvas(aCanvas);
    adinkra = [];
    for(let i=0;i<22;i++){
        adinkra.push({
            x: Math.random()*aCanvas.width,
            y: Math.random()*aCanvas.height,
            size: 10 + Math.random()*6,
            speed: 0.3 + Math.random()*0.4,
            char: symbols[Math.floor(Math.random()*symbols.length)]
        });
    }
}
function animateAdinkra(){
    fitCanvas(aCanvas);
    actx.clearRect(0,0,aCanvas.width,aCanvas.height);
    actx.fillStyle = "rgba(255,215,0,0.9)";
    adinkra.forEach(s=>{
        actx.font = s.size + "px serif";
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

/* RINGS */
const rCanvas = document.getElementById("ringsCanvas");
const rctx = rCanvas.getContext("2d");

function animateRings(){
    fitCanvas(rCanvas);
    const w=rCanvas.width, h=rCanvas.height;
    rctx.clearRect(0,0,w,h);

    const cx = w * 0.70;
    const cy = h * 0.52;
    const t  = Date.now() * 0.00005;

    for (let i=0;i<3;i++){
        const R = 130 + i*40;
        rctx.beginPath();
        rctx.arc(cx, cy, R, 0, Math.PI*2);
        rctx.strokeStyle = "rgba(255,215,0," + (0.35 - i*0.1) + ")";
        rctx.lineWidth = 3;

        rctx.save();
        rctx.translate(cx,cy);
        rctx.rotate((i%2===0?1:-1)*t);
        rctx.translate(-cx,-cy);
        rctx.stroke();
        rctx.restore();
    }
    requestAnimationFrame(animateRings);
}
animateRings();

/* 3D AVATAR */
const avatarCanvas = document.getElementById("avatarCanvas");
const renderer = new THREE.WebGLRenderer({canvas: avatarCanvas, alpha:true});
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
camera.position.set(0, 1.05, 2.2);

const keyLight = new THREE.DirectionalLight(0xf6d47a, 1.2);
keyLight.position.set(2,3,4);
scene.add(keyLight);
scene.add(new THREE.AmbientLight(0xffffff,0.4));

let avatar = null;
const loader = new THREE.GLTFLoader();

loader.load(
    "https://models.readyplayer.me/691a48795f9f523e503e7810.glb",
    gltf => {
        avatar = gltf.scene;
        avatar.scale.set(1.45,1.45,1.45);
        avatar.position.y = -1.20;
        scene.add(avatar);
    }
);

let dragging = false, prevX = 0, rot = 0.004;
avatarCanvas.addEventListener("mousedown", e => { dragging = true; prevX = e.clientX; });
window.addEventListener("mouseup", () => { dragging = false; });
window.addEventListener("mousemove", e => {
    if (dragging && avatar) {
        rot = (e.clientX - prevX) * 0.0004;
        prevX = e.clientX;
    }
});

function animateAvatar(){
    requestAnimationFrame(animateAvatar);
    if (avatar) avatar.rotation.y += rot;
    renderer.setSize(avatarCanvas.clientWidth, avatarCanvas.clientHeight);
    renderer.render(scene, camera);
}
animateAvatar();

/* NAVBAR → STREAMLIT */
function sendPanel(name){
    window.parent.postMessage({panel: name}, "*");
}
</script>
"""

# Make the iframe exactly viewport height (no outer scroll)
components.html(hero_html, height=768, scrolling=False)

# --------------------------------------------------------
# SLIDING PANELS
# --------------------------------------------------------
panel_engine = """
<style>
.panel {
    position: fixed;
    top:0;
    left:100vw;
    width:100vw;
    height:100vh;
    background:rgba(10,10,10,0.85);
    backdrop-filter:blur(20px);
    transition:0.3s ease;
    z-index:99999999;
    padding:120px;
    color:white;
}
.panel.active { left:0; }

.close-btn {
    position:absolute;
    top:40px;
    right:40px;
    font-size:38px;
    cursor:pointer;
}

.panel-title {
    font-size:52px;
    font-weight:900;
    margin-bottom:20px;
    background:linear-gradient(to right,#f6d47a,#fff);
    -webkit-background-clip:text;
    color:transparent;
}

.panel-body {
    font-size:20px;
    width:60%;
}
</style>

<div id="panel" class="panel">
    <div class="close-btn" onclick="closePanel()">×</div>
    <div id="panelContent"></div>
</div>

<script>
window.addEventListener("message", event=>{
    if(event.data.panel){ openPanel(event.data.panel); }
});

function openPanel(name){
    fetch("/panel?name="+name)
    .then(r=>r.text())
    .then(html=>{
        document.getElementById("panelContent").innerHTML=html;
        document.getElementById("panel").classList.add("active");
    });
}

function closePanel(){
    document.getElementById("panel").classList.remove("active");
}
</script>
"""
components.html(panel_engine, height=0, scrolling=False)

# --------------------------------------------------------
# PANEL CONTENTS
# --------------------------------------------------------
def panel_html(title, body):
    return f"""
    <div class='panel-title'>{title}</div>
    <div class='panel-body'>{body}</div>
    """

panels = {
    "Projects": panel_html(
        "Projects",
        """
        <p><b>🔹 Titanic Survival Predictor</b></p>
        <p><b>🔹 AQI Predictor</b></p>
        <p><b>🔹 Mental Health Predictor</b></p>
        <p><b>🔹 KukiLabs AI Tools</b></p>
        """,
    ),
    "About": panel_html(
        "About Me",
        """
        I am <b>Mark Chweya</b>, a Data Science & AI developer building predictive models,
        analytics pipelines, and futuristic African UI experiences.
        """,
    ),
    "Resume": panel_html(
        "Resume",
        """
        <b>Education</b><br>
        • USIU–Africa — Data Science<br><br>
        <b>Skills</b><br>
        Python, ML, Streamlit, AI Systems
        """,
    ),
    "Contact": panel_html(
        "Contact Me",
        """
        Email: <span style='color:#f6d47a;'>chweyamark@gmail.com</span><br>
        Phone: <span style='color:#f6d47a;'>+254 703 951 840</span>
        """,
    ),
}

# --------------------------------------------------------
# PANEL ROUTE HANDLER
# --------------------------------------------------------
name = st.query_params.get("name", None)
if name in panels:
    st.markdown(panels[name], unsafe_allow_html=True)
