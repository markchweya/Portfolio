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
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

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
html, body {
    margin: 0;
    padding: 0;
    height: 100vh;
    background: #0d0f13;
    overflow: hidden;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* HERO container */
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

/* BACKPACK NAV – draggable */
.bag-nav {
    position: absolute;
    width: 120px;
    height: 120px;
    z-index: 30;
    user-select: none;
}

/* BACKPACK ICON */
#bagIcon {
    position: absolute;
    top: 16px;
    left: 16px;
    width: 88px;
    height: 88px;
    cursor: grab;
    border-radius: 32px;
    background: radial-gradient(circle at 30% 0%, rgba(255,215,0,0.52), rgba(10,10,10,0.98));
    box-shadow:
        0 0 40px rgba(255,215,0,0.45),
        0 24px 50px rgba(0,0,0,0.9);
    backdrop-filter: blur(24px);
    transition: box-shadow 0.25s ease;
    transform-origin: 50% 50%;
}
#bagIcon:active {
    cursor: grabbing;
}

/* bag body */
.bag-body {
    position: absolute;
    inset: 18px 14px 20px 14px;
    border-radius: 22px;
    background: radial-gradient(circle at 30% 0%, #333, #050505);
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

/* breathing glow */
#bagIcon {
    animation: bagPulse 2.8s ease-in-out infinite;
}
@keyframes bagPulse {
    0%, 100% { box-shadow: 0 0 40px rgba(255,215,0,0.35), 0 24px 50px rgba(0,0,0,0.9); }
    50%      { box-shadow: 0 0 55px rgba(255,215,0,0.6), 0 28px 60px rgba(0,0,0,1); }
}

/* BAG MENU (sticks to bag) */
.bag-menu {
    position: absolute;
    top: 104px;
    left: 50%;
    transform: translateX(-50%) translateY(-10px) scale(0.96);
    padding: 10px 20px;
    border-radius: 20px;
    background: rgba(7,7,7,0.96);
    backdrop-filter: blur(18px);
    display: flex;
    gap: 18px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease, transform 0.25s ease;
    box-shadow: 0 18px 40px rgba(0,0,0,0.85);
    border: 1px solid rgba(255,215,0,0.15);
}
.bag-menu.open {
    opacity: 1;
    transform: translateX(-50%) translateY(0) scale(1);
    pointer-events: auto;
}

/* floating nav items */
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

/* MAIN CONTENT */
.center-row {
    flex: 1;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 140px;
    transform: translateY(40px);
}

/* LEFT TEXT */
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
    position: relative;
    font-size: 70px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 24px rgba(246,212,122,0.4);
    overflow: hidden;
}

/* SHARP LIGHT STREAK ACROSS NAME */
.hero-name::before {
    content: "";
    position: absolute;
    top: -20%;
    left: -130%;
    width: 60%;
    height: 140%;
    background: linear-gradient(120deg,
        rgba(0,0,0,0) 0%,
        rgba(255,255,255,0.0) 20%,
        rgba(255,255,255,0.75) 50%,
        rgba(255,215,0,0.0) 80%,
        rgba(0,0,0,0) 100%);
    mix-blend-mode: screen;
    filter: blur(2px);
    animation: nameShine 3.6s ease-in-out infinite;
}
@keyframes nameShine {
    from { left: -130%; }
    to   { left: 140%; }
}

/* SUBTITLE – smaller + less spaced */
.hero-role {
    font-size: 22px;
    color: #eaeaea;
    margin-top: -4px;
    opacity: 0;
    transform: translateY(16px);
    filter: blur(6px);
    letter-spacing: 0.18em;
    animation: roleIn 0.9s ease-out forwards;
    animation-delay: 0.25s;
}
@keyframes roleIn {
    from { opacity: 0; transform: translateY(16px); filter: blur(6px); letter-spacing: 0.18em; }
    to   { opacity: 1; transform: translateY(0);  filter: blur(0);  letter-spacing: 0.05em; }
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

/* BACKGROUND CANVASES */
#codeCanvas, #ringsCanvas {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    opacity: 0;
    animation: bgIn 0.9s ease-out forwards;
}
#codeCanvas { animation-delay: 0.1s; }
#ringsCanvas { animation-delay: 0.25s; }

@keyframes bgIn {
    from { opacity: 0; filter: blur(4px); }
    to   { opacity: 1; filter: blur(0); }
}
</style>

<div class="hero-wrap">

    <!-- DRAGGABLE BACKPACK + MENU -->
    <div class="bag-nav" id="bagNav">
        <div id="bagIcon">
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

    <!-- BACKGROUND TECH + RINGS -->
    <canvas id="codeCanvas"></canvas>
    <canvas id="ringsCanvas"></canvas>

    <!-- CENTERED CONTENT -->
    <div class="center-row">
        <div class="hero-text">
            <div class="hero-name">Mark Chweya</div>
            <div class="hero-role">Data Science &amp; Artificial Intelligence</div>
        </div>
        <canvas id="avatarCanvas"></canvas>
    </div>
</div>

<!-- THREE.JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>

<script>
/* Make iframe match viewport height */
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

/* Generic canvas resize */
function fitCanvas(c){
    const w = c.clientWidth, h = c.clientHeight;
    if (c.width !== w || c.height !== h) {
        c.width = w;
        c.height = h;
    }
}

/* ------------------ DRAGGABLE / PHYSICS BACKPACK ------------------ */
const bagNav = document.getElementById("bagNav");
const bagIcon = document.getElementById("bagIcon");
const bagMenu = document.getElementById("bagMenu");

let bagX = window.innerWidth / 2 - 60;
let bagY = 20;
bagNav.style.left = bagX + "px";
bagNav.style.top = bagY + "px";

let vx = 0, vy = 0;
let draggingBag = false;
let dragOffsetX = 0, dragOffsetY = 0;
let lastMouseX = 0, lastMouseY = 0;
let lastMoveTime = 0;
let clickCandidate = false;
let totalDragDist = 0;

function toggleBagMenu(){
    bagMenu.classList.toggle("open");
}

bagIcon.addEventListener("mousedown", (e) => {
    draggingBag = true;
    clickCandidate = true;
    totalDragDist = 0;
    vx = vy = 0;
    dragOffsetX = e.clientX - bagX;
    dragOffsetY = e.clientY - bagY;
    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
    lastMoveTime = Date.now();
});

window.addEventListener("mousemove", (e) => {
    if (!draggingBag) return;
    const now = Date.now();
    const dt = Math.max(now - lastMoveTime, 1);
    const dx = e.clientX - lastMouseX;
    const dy = e.clientY - lastMouseY;

    bagX = e.clientX - dragOffsetX;
    bagY = e.clientY - dragOffsetY;

    bagNav.style.left = bagX + "px";
    bagNav.style.top = bagY + "px";

    vx = dx / dt * 16;
    vy = dy / dt * 16;

    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
    lastMoveTime = now;

    totalDragDist += Math.sqrt(dx*dx + dy*dy);
    if (totalDragDist > 5) clickCandidate = false;
});

window.addEventListener("mouseup", () => {
    if (draggingBag && clickCandidate) {
        toggleBagMenu();
    }
    draggingBag = false;
});

/* FLOATING physics (no gravity, just inertia + bounces) */
function animateBag(){
    const padding = 10;
    if (!draggingBag) {
        // no gravity – just inertia + friction
        bagX += vx;
        bagY += vy;

        const maxX = window.innerWidth - bagNav.offsetWidth - padding;
        const maxY = window.innerHeight - bagNav.offsetHeight - padding;

        if (bagX < padding) {
            bagX = padding;
            vx = -vx * 0.7;
        } else if (bagX > maxX) {
            bagX = maxX;
            vx = -vx * 0.7;
        }
        if (bagY < padding) {
            bagY = padding;
            vy = -vy * 0.7;
        } else if (bagY > maxY) {
            bagY = maxY;
            vy = -vy * 0.7;
        }

        // friction
        vx *= 0.985;
        vy *= 0.985;

        bagNav.style.left = bagX + "px";
        bagNav.style.top = bagY + "px";

        const angle = vx * 1.2;
        bagIcon.style.transform = "rotate(" + angle + "deg)";
    }
    requestAnimationFrame(animateBag);
}
animateBag();

/* ------------------ CODE / DATA BACKGROUND (UNIQUE TOKENS) ------------------ */
const codeCanvas = document.getElementById("codeCanvas");
const codeCtx = codeCanvas.getContext("2d");

let codeParticles = [];

function randomToken() {
    const chars = "01xyzλΣμσπ∂µσπ{}()[]+-*/<>:=._#";
    const len = 3 + Math.floor(Math.random() * 6);
    let s = "";
    for (let i = 0; i < len; i++) {
        s += chars[Math.floor(Math.random() * chars.length)];
    }
    return s;
}

function generateUniqueToken(existingTokens) {
    let token;
    do {
        token = randomToken();
    } while (existingTokens.indexOf(token) !== -1);
    return token;
}

function initCode(){
    fitCanvas(codeCanvas);
    codeParticles = [];
    const count = 40;
    for (let i = 0; i < count; i++){
        const existing = codeParticles.map(p => p.token);
        codeParticles.push({
            x: Math.random() * codeCanvas.width,
            y: Math.random() * codeCanvas.height,
            speed: 0.3 + Math.random() * 0.7,
            size: 10 + Math.random() * 6,
            token: generateUniqueToken(existing),
            alpha: 0.25 + Math.random() * 0.4
        });
    }
}

function animateCode(){
    fitCanvas(codeCanvas);
    codeCtx.clearRect(0,0,codeCanvas.width,codeCanvas.height);
    const existingNow = codeParticles.map(p => p.token);

    codeParticles.forEach((p, idx) => {
        codeCtx.font = p.size + "px 'JetBrains Mono', monospace";
        codeCtx.fillStyle = "rgba(255,215,0," + p.alpha + ")";
        codeCtx.fillText(p.token, p.x, p.y);

        p.y += p.speed;
        p.x += p.speed * 0.1;

        if (p.y > codeCanvas.height + 40) {
            p.y = -20;
            p.x = Math.random() * codeCanvas.width;

            // regenerate a brand new unique token
            const others = codeParticles
                .filter((_, j) => j !== idx)
                .map(q => q.token);
            p.token = generateUniqueToken(others);
        }
    });
    requestAnimationFrame(animateCode);
}
initCode();
animateCode();

/* ------------------ RINGS – rotating with different speeds ------------------ */
const rCanvas = document.getElementById("ringsCanvas");
const rctx = rCanvas.getContext("2d");

function animateRings(){
    fitCanvas(rCanvas);
    const w = rCanvas.width, h = rCanvas.height;
    rctx.clearRect(0,0,w,h);

    const cx = w * 0.70;
    const cy = h * 0.64;
    const t  = Date.now() * 0.00004;

    const speeds = [0.6, -0.4, 0.25];

    for (let i=0;i<3;i++){
        const R = 130 + i*40;
        const alpha = 0.35 - i*0.1;

        rctx.save();
        rctx.translate(cx,cy);
        rctx.rotate(t * speeds[i]);
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

/* ------------------ 3D AVATAR ------------------ */
const avatarCanvas = document.getElementById("avatarCanvas");
const renderer = new THREE.WebGLRenderer({canvas: avatarCanvas, alpha:true});
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
camera.position.set(0, 1.1, 2.5);

/* Lights */
const keyLight = new THREE.DirectionalLight(0xffffff, 2.1);
keyLight.position.set(2.4, 3.2, 4.0);
scene.add(keyLight);

const fillLight = new THREE.DirectionalLight(0xffffff, 1.2);
fillLight.position.set(-2.0, 2.5, 1.8);
scene.add(fillLight);

const rimLight = new THREE.DirectionalLight(0xffd980, 0.8);
rimLight.position.set(-2.5, 1.5, -3.0);
scene.add(rimLight);

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
    err => { console.error("Error loading avatar:", err); }
);

let draggingAvatar = False = false, prevX = 0, rot = 0.004;
avatarCanvas.addEventListener("mousedown", e => { draggingAvatar = true; prevX = e.clientX; });
window.addEventListener("mouseup", () => { draggingAvatar = false; });
window.addEventListener("mousemove", e => {
    if (draggingAvatar && avatar) {
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

/* STREAMLIT PANEL MESSAGES */
function sendPanel(name){
    window.parent.postMessage({panel: name}, "*");
}
</script>
"""

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
        I am <b>Mark Chweya</b>, a Data Science &amp; AI developer building predictive models,
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
