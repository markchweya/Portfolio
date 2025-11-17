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
# GLOBAL CSS – LOCK APP TO 100vh, NO SCROLL
# --------------------------------------------------------
st.markdown(
    """
<style>
/* Hide default Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

/* Root layout containers – force them to 100vh and hide scroll */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    height: 100vh !important;
    overflow: hidden !important;
    background: #0d0f13 !important;
}

#root,
[data-testid="stAppViewContainer"],
section.main,
.block-container {
    margin: 0 !important;
    padding: 0 !important;
    height: 100vh !important;
    max-height: 100vh !important;
    overflow: hidden !important;
    max-width: 100% !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------------
# HERO SECTION — BACKPACK NAV + NAME + AVATAR
# --------------------------------------------------------
hero_html = """
<style>
/* Inside iframe */
html, body {
    margin: 0;
    padding: 0;
    height: 100vh;
    background: #0d0f13;
    overflow: hidden;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* HERO wraps full viewport inside iframe */
.hero-wrap {
    position: relative;
    width: 100%;
    height: 100vh;
    background: #0d0f13;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    overflow: hidden;
    animation: heroIn 0.8s ease-out forwards;
    opacity: 0;
}
@keyframes heroIn {
    from { opacity: 0; transform: translateY(10px) scale(0.98); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}

/* BACKPACK NAV – upgraded look */
.bag-nav {
    position: absolute;
    top: 28px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 30;
    user-select: none;
}

/* backpack icon */
.bag-icon {
    position: relative;
    width: 88px;
    height: 88px;
    cursor: pointer;
    border-radius: 32px;
    background: radial-gradient(circle at 30% 0%, rgba(255,215,0,0.45), rgba(10,10,10,0.98));
    box-shadow:
        0 0 40px rgba(255,215,0,0.45),
        0 24px 50px rgba(0,0,0,0.9);
    backdrop-filter: blur(24px);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

/* bag body */
.bag-body {
    position: absolute;
    inset: 18px 14px 20px 14px;
    border-radius: 22px;
    background: linear-gradient(180deg, #181818, #050505);
    border: 1px solid rgba(255,215,0,0.4);
    box-shadow: inset 0 0 20px rgba(0,0,0,0.9);
}

/* pocket */
.bag-pocket {
    position: absolute;
    left: 20px;
    right: 20px;
    bottom: 18px;
    height: 22px;
    border-radius: 12px;
    background: linear-gradient(180deg, #252525, #111111);
    border: 1px solid rgba(255,215,0,0.4);
}

/* flap */
.bag-flap {
    position: absolute;
    top: 13px;
    left: 20px;
    right: 20px;
    height: 20px;
    border-radius: 16px 16px 12px 12px;
    background: linear-gradient(180deg, #303030, #151515);
    border: 1px solid rgba(255,215,0,0.45);
}

/* straps */
.bag-strap-left,
.bag-strap-right {
    position: absolute;
    top: 10px;
    width: 14px;
    height: 20px;
    border-radius: 999px;
    border: 2px solid rgba(255,215,0,0.6);
    border-bottom: none;
}
.bag-strap-left { left: 20px; }
.bag-strap-right { right: 20px; }

/* glowing dot on bag (indicator) */
.bag-dot {
    position: absolute;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    width: 7px;
    height: 7px;
    border-radius: 999px;
    background: rgba(255,215,0,0.95);
    box-shadow: 0 0 14px rgba(255,215,0,1);
}

/* subtle breathing animation */
.bag-icon {
    animation: bagPulse 2.8s ease-in-out infinite;
}
@keyframes bagPulse {
    0%, 100% { transform: translateY(0); box-shadow: 0 0 40px rgba(255,215,0,0.35), 0 24px 50px rgba(0,0,0,0.9); }
    50%      { transform: translateY(-3px); box-shadow: 0 0 55px rgba(255,215,0,0.55), 0 28px 60px rgba(0,0,0,1); }
}

/* BAG MENU */
.bag-menu {
    margin-top: 12px;
    padding: 10px 20px;
    border-radius: 20px;
    background: rgba(7,7,7,0.96);
    backdrop-filter: blur(18px);
    display: flex;
    gap: 18px;
    opacity: 0;
    transform: translateY(-10px) scale(0.96);
    pointer-events: none;
    transition: opacity 0.25s ease, transform 0.25s ease;
    box-shadow: 0 18px 40px rgba(0,0,0,0.85);
    border: 1px solid rgba(255,215,0,0.15);
}

.bag-menu.open {
    opacity: 1;
    transform: translateY(0) scale(1);
    pointer-events: auto;
}

/* items look like floating text with underline effect */
.bag-item {
    position: relative;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 0.05em;
    color: #f7df8b;
    cursor: pointer;
    padding: 4px 2px;
    text-transform: none;
    transition: color 0.25s ease, transform 0.25s ease;
    user-select: none;
}

.bag-item::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: -3px;
    transform: translateX(-50%);
    width: 0;
    height: 2px;
    border-radius: 999px;
    background: linear-gradient(90deg, #f6d47a, #ffffff);
    box-shadow: 0 0 10px rgba(255,215,0,0.85);
    transition: width 0.25s ease;
}

.bag-item:hover {
    color: #ffffff;
    transform: translateY(-1px);
}
.bag-item:hover::after {
    width: 70%;
}

/* MAIN CONTENT ROW */
.center-row {
    flex: 1;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 140px;
    transform: translateY(40px);
}

/* LEFT — NAME + ROLE (with smoother animations) */
.hero-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    animation: textIn 0.85s ease-out forwards;
    opacity: 0;
}
@keyframes textIn {
    from { opacity: 0; transform: translateX(-40px); filter: blur(6px); }
    to   { opacity: 1; transform: translateX(0); filter: blur(0); }
}

.hero-name {
    font-size: 70px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 24px rgba(246,212,122,0.4);
}

/* subtitle animation – drift up + letter spacing easing */
.hero-role {
    font-size: 28px;
    color: #eaeaea;
    margin-top: -8px;
    opacity: 0;
    transform: translateY(16px);
    filter: blur(6px);
    letter-spacing: 0.24em;
    animation: roleIn 0.9s ease-out forwards;
    animation-delay: 0.25s;
}
@keyframes roleIn {
    from { opacity: 0; transform: translateY(16px); filter: blur(6px); letter-spacing: 0.24em; }
    to   { opacity: 1; transform: translateY(0);  filter: blur(0);  letter-spacing: 0.04em; }
}

/* RIGHT — AVATAR */
#avatarCanvas {
    width: 420px;
    height: 540px;
    z-index: 5;
    opacity: 0;
    transform: translateY(25px) scale(0.97);
    animation: avatarIn 0.9s ease-out forwards;
    animation-delay: 0.2s;
}
@keyframes avatarIn {
    from { opacity: 0; transform: translateY(25px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}

/* BACKGROUND CANVASES (fill full viewport) */
#ringsCanvas, #adinkraCanvas {
    position: absolute;
    left: 0; 
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    opacity: 0;
    animation: bgIn 0.9s ease-out forwards;
}
#adinkraCanvas { animation-delay: 0.15s; }
#ringsCanvas   { animation-delay: 0.25s; }

@keyframes bgIn {
    from { opacity: 0; filter: blur(4px); }
    to   { opacity: 1; filter: blur(0); }
}
</style>

<div class="hero-wrap">

    <!-- BACKPACK NAV -->
    <div class="bag-nav">
        <div class="bag-icon" onclick="toggleBagMenu()">
            <div class="bag-body"></div>
            <div class="bag-pocket"></div>
            <div class="bag-flap"></div>
            <div class="bag-strap-left"></div>
            <div class="bag-strap-right"></div>
            <div class="bag-dot"></div>
        </div>
        <div class="bag-menu" id="bagMenu">
            <span class="bag-item" onclick="sendPanel('Home')">Home</span>
            <span class="bag-item" onclick="sendPanel('Projects')">Projects</span>
            <span class="bag-item" onclick="sendPanel('About')">About</span>
            <span class="bag-item" onclick="sendPanel('Resume')">Resume</span>
            <span class="bag-item" onclick="sendPanel('Contact')">Contact</span>
        </div>
    </div>

    <!-- BACKGROUND ANIMATIONS -->
    <canvas id="adinkraCanvas"></canvas>
    <canvas id="ringsCanvas"></canvas>

    <!-- CENTERED CONTENT -->
    <div class="center-row">
        <!-- NAME + ROLE -->
        <div class="hero-text">
            <div class="hero-name">Mark Chweya</div>
            <div class="hero-role">Data Science &amp; Artificial Intelligence</div>
        </div>

        <!-- AVATAR -->
        <canvas id="avatarCanvas"></canvas>
    </div>

</div>

<!-- THREE.JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>

<script>
/* Make iframe always exactly viewport height → no outer scroll */
function resizeFrame() {
    try {
        if (window.frameElement) {
            window.frameElement.style.height = window.innerHeight + "px";
        }
    } catch (e) {}
}
window.addEventListener("load", resizeFrame);
window.addEventListener("resize", resizeFrame);
resizeFrame();

/* Helper: fit canvases */
function fitCanvas(c){
    const w = c.clientWidth, h = c.clientHeight;
    if (c.width !== w || c.height !== h) {
        c.width = w;
        c.height = h;
    }
}

/* ------------------ BACKPACK MENU TOGGLE ------------------ */
function toggleBagMenu(){
    const menu = document.getElementById("bagMenu");
    menu.classList.toggle("open");
}

/* ------------------ ADINKRA PARTICLES ------------------ */
const aCanvas = document.getElementById("adinkraCanvas");
const actx = aCanvas.getContext("2d");
const symbols = ["✺","✤","❂"];
let adinkra = [];

function initAdinkra(){
    fitCanvas(aCanvas);
    adinkra = [];
    for(let i=0;i<26;i++){
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

/* ------------------ RINGS – all rotating, different speeds & directions ------------------ */
const rCanvas = document.getElementById("ringsCanvas");
const rctx = rCanvas.getContext("2d");

function animateRings(){
    fitCanvas(rCanvas);
    const w=rCanvas.width, h=rCanvas.height;
    rctx.clearRect(0,0,w,h);

    const cx = w * 0.70;
    const cy = h * 0.64;
    const t  = Date.now() * 0.00004;  // global time

    // three rings, each with its own speed + direction
    const speeds = [0.6, -0.4, 0.25];

    for (let i=0;i<3;i++){
        const R = 130 + i*40;
        const alpha = 0.35 - i*0.1;

        rctx.save();
        rctx.translate(cx,cy);
        rctx.rotate(t * speeds[i]);  // slow rotation, each different
        rctx.beginPath();
        rctx.arc(0, 0, R, 0, Math.PI*2);
        rctx.strokeStyle = "rgba(255,215,0," + alpha + ")";
        rctx.lineWidth = 3;
        rctx.stroke();
        rctx.restore();
    }
    requestAnimationFrame(animateRings);
}
animateRings();

/* ------------------ 3D AVATAR – brighter + more visible ------------------ */
const avatarCanvas = document.getElementById("avatarCanvas");
const renderer = new THREE.WebGLRenderer({canvas: avatarCanvas, alpha:true});
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
camera.position.set(0, 1.1, 2.5);

/* KEY LIGHT – strong from front-right */
const keyLight = new THREE.DirectionalLight(0xffffff, 2.1);
keyLight.position.set(2.4, 3.2, 4.0);
scene.add(keyLight);

/* FILL LIGHT – from left to soften shadows */
const fillLight = new THREE.DirectionalLight(0xffffff, 1.2);
fillLight.position.set(-2.0, 2.5, 1.8);
scene.add(fillLight);

/* RIM LIGHT – from behind for outline */
const rimLight = new THREE.DirectionalLight(0xffd980, 0.8);
rimLight.position.set(-2.5, 1.5, -3.0);
scene.add(rimLight);

/* AMBIENT – lift everything */
const ambient = new THREE.AmbientLight(0xffffff, 0.9);
scene.add(ambient);

let avatar = null;
const loader = new THREE.GLTFLoader();

loader.load(
    "https://models.readyplayer.me/691ac987786317131c914b96.glb",
    gltf => {
        avatar = gltf.scene;
        avatar.scale.set(1.7,1.7,1.7);
        avatar.position.y = -1.3;
        scene.add(avatar);
    },
    undefined,
    err => {
        console.error("Error loading avatar:", err);
    }
);

// Mouse drag to control spin speed
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

/* NAV MENU → STREAMLIT PANELS */
function sendPanel(name){
    window.parent.postMessage({panel: name}, "*");
}
</script>
"""

# Initial height is arbitrary; JS inside iframe resizes it to viewport height
components.html(hero_html, height=600, scrolling=False)

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
