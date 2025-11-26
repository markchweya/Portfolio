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
# (FIX: make the FIRST components.html iframe truly fullscreen and cover Streamlit's top reserved band)
# --------------------------------------------------------
st.markdown(
    """
<style>
#MainMenu, footer, header {display: none !important;} /* display:none so NO reserved space */
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stHeader"] {display:none !important; height:0 !important;}

/* Remove Streamlit's top padding that can remain even if header is hidden */
[data-testid="stApp"] {margin:0 !important; padding:0 !important;}
[data-testid="stAppViewContainer"] {margin:0 !important; padding-top:0 !important;}
section.main {margin:0 !important; padding-top:0 !important;}
.block-container {margin:0 !important; padding:0 !important; max-width:100% !important;}

html, body {
    margin: 0 !important;
    padding: 0 !important;
    height: 100vh !important;
    overflow: hidden !important;
    background: #0d0f13 !important;
}

/* Kill all extra padding/margins around Streamlit main area */
#root,
[data-testid="stAppViewContainer"],
section.main,
.block-container,
div[role="main"] {
    margin: 0 !important;
    padding: 0 !important;
    height: 100vh !important;
    max-height: 100vh !important;
    overflow: hidden !important;
    max-width: 100% !important;
}

/* ------------------ HARD CLAMP: FIRST HTML IFRAME FULLSCREEN (NO TOP GAP) ------------------ */
/* Streamlit sometimes keeps a top band; we COVER it by pinning the iframe to the viewport */
div[data-testid="stHtml"]:first-of-type{
    margin: 0 !important;
    padding: 0 !important;
    height: 0 !important;          /* no layout push */
    line-height: 0 !important;
}

/* Overshoot upward to cover the stubborn top black band */
div[data-testid="stHtml"]:first-of-type iframe{
    position: fixed !important;
    top: -90px !important;                          /* <-- covers Streamlit reserved band */
    left: 0 !important;
    width: 100vw !important;
    height: calc(100vh + 90px) !important;          /* keep bottom covered too */
    margin: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    display: block !important;
    background: transparent !important;
    z-index: 9999 !important;
}

/* Keep any other HTML components (like your hidden panel engine) normal/inert */
div[data-testid="stHtml"]:not(:first-of-type) iframe {
    position: static !important;
    inset: auto !important;
    width: 0 !important;
    height: 0 !important;
    border: 0 !important;
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
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(circle at 20% 0%, #161922, #050609);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    overflow: hidden;
    animation: heroIn 0.8s ease-out forwards;
    opacity: 0;
}

/* global glossy overlay */
.hero-wrap::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 20% 0%, rgba(255,255,255,0.08), transparent 55%),
        radial-gradient(circle at 80% 100%, rgba(255,215,0,0.12), transparent 55%),
        linear-gradient(120deg, rgba(255,255,255,0.04), rgba(255,255,255,0.0) 40%);
    mix-blend-mode: screen;
    opacity: 0.9;
    pointer-events: none;
    z-index: 0;
}

/* no vertical push, just a subtle scale in */
@keyframes heroIn {
    from { opacity: 0; transform: scale(0.98); }
    to   { opacity: 1; transform: scale(1); }
}

/* BACKPACK NAV – draggable wrapper */
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
    background:
        radial-gradient(circle at 30% 0%, rgba(255,215,0,0.70), rgba(10,10,10,0.98));
    box-shadow:
        0 0 45px rgba(255,215,0,0.55),
        0 24px 50px rgba(0,0,0,0.9),
        inset 0 0 16px rgba(0,0,0,0.9);
    backdrop-filter: blur(24px);
    transition: box-shadow 0.25s ease, transform 0.15s ease;
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
    background: radial-gradient(circle at 30% 0%, #3a3a3a, #050505);
    border: 1px solid rgba(255,215,0,0.45);
    box-shadow:
        inset 0 0 20px rgba(0,0,0,0.9),
        0 0 16px rgba(255,255,255,0.08);
}

/* pocket */
.bag-pocket {
    position: absolute;
    left: 20px;
    right: 20px;
    bottom: 18px;
    height: 22px;
    border-radius: 12px;
    background: linear-gradient(180deg, #2b2b2b, #101010);
    border: 1px solid rgba(255,215,0,0.45);
}

/* flap */
.bag-flap {
    position: absolute;
    top: 13px;
    left: 20px;
    right: 20px;
    height: 20px;
    border-radius: 16px 16px 12px 12px;
    background: linear-gradient(180deg, #3a3a3a, #181818);
    border: 1px solid rgba(255,215,0,0.5);
}

/* straps */
.bag-strap-left,
.bag-strap-right {
    position: absolute;
    top: 10px;
    width: 14px;
    height: 20px;
    border-radius: 999px;
    border: 2px solid rgba(255,215,0,0.7);
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
    background: rgba(255,215,0,0.98);
    box-shadow:
        0 0 14px rgba(255,215,0,1),
        0 0 40px rgba(255,215,0,0.7);
}

/* breathing glow */
#bagIcon {
    animation: bagPulse 2.8s ease-in-out infinite;
}
@keyframes bagPulse {
    0%, 100% {
        box-shadow:
            0 0 38px rgba(255,215,0,0.45),
            0 24px 50px rgba(0,0,0,0.9),
            inset 0 0 12px rgba(0,0,0,0.8);
    }
    50% {
        box-shadow:
            0 0 60px rgba(255,215,0,0.8),
            0 28px 60px rgba(0,0,0,1),
            inset 0 0 18px rgba(0,0,0,0.9);
    }
}

/* BAG MENU (sticks to bag) */
.bag-menu {
    position: absolute;
    top: 104px;
    left: 50%;
    transform: translateX(-50%) translateY(-10px) scale(0.96);
    padding: 10px 20px;
    border-radius: 20px;
    background: radial-gradient(circle at 0% 0%, rgba(255,255,255,0.18), rgba(7,7,7,0.99));
    backdrop-filter: blur(18px);
    display: flex;
    gap: 18px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease, transform 0.25s ease, box-shadow 0.3s ease;
    box-shadow:
        0 18px 40px rgba(0,0,0,0.85),
        0 0 24px rgba(255,215,0,0.28);
}
.bag-menu.open {
    opacity: 1;
    transform: translateX(-50%) translateY(0) scale(1);
    pointer-events: auto;
}

/* border hit glow */
.bag-hit-glow {
    box-shadow:
        0 0 32px rgba(255,215,0,0.95),
        0 0 90px rgba(255,215,0,0.55),
        0 20px 60px rgba(0,0,0,0.9) !important;
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
    transform: translateY(0);
    position: relative;
    z-index: 2;
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
    text-shadow:
        0 0 24px rgba(246,212,122,0.4),
        0 0 40px rgba(0,0,0,0.9);
    overflow: hidden;
}

/* CODE FEED LAYER BEHIND NAME */
.hero-name::after {
    content: "01λΣµσπ{}[]<>/\\\\|=_+*# 01λΣµσπ{}[]<>/\\\\|=_+*#";
    position: absolute;
    inset: -4px 0;
    background: linear-gradient(120deg,
        rgba(0,0,0,0),
        rgba(255,215,0,0.7),
        rgba(255,255,255,0.8),
        rgba(0,0,0,0));
    mix-blend-mode: screen;
    opacity: 0.55;
    pointer-events: none;
    animation: nameCodeFlow 4s linear infinite;
    -webkit-mask-image: linear-gradient(90deg, rgba(0,0,0,1), rgba(0,0,0,0.5), rgba(0,0,0,0));
    mask-image: linear-gradient(90deg, rgba(0,0,0,1), rgba(0,0,0,0.5), rgba(0,0,0,0));
}
@keyframes nameCodeFlow {
    from { transform: translateX(22px); }
    to   { transform: translateX(-22px); }
}

/* once decoded, name "sheds" the code feed */
.hero-name.decoded::after {
    opacity: 0;
    transition: opacity 0.55s ease-out;
}

/* SHARP LIGHT STREAK ACROSS NAME – only when .shine class is present */
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
    opacity: 0;
}
.hero-name.shine::before {
    opacity: 1;
    animation: nameShine 3.6s ease-in-out forwards;
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

/* RIGHT — AVATAR: base state only, animation via random classes */
#avatarCanvas {
    width: 420px;
    height: 540px;
    z-index: 5;
    opacity: 0;
    transform: translateY(25px) scale(0.97);
}

/* random left entry */
.avatar-enter-left {
    animation: avatarInLeft 0.9s ease-out forwards;
}
@keyframes avatarInLeft {
    from { opacity: 0; transform: translate(-50px, 25px) scale(0.9); }
    to   { opacity: 1; transform: translate(0px, 0px) scale(0.98); }
}

/* random right entry */
.avatar-enter-right {
    animation: avatarInRight 0.9s ease-out forwards;
}
@keyframes avatarInRight {
    from { opacity: 0; transform: translate(50px, 25px) scale(0.9); }
    to   { opacity: 1; transform: translate(0px, 0px) scale(0.98); }
}

/* EXTRA SYNC ANIMATION WHEN NAME FINISHES */
#avatarCanvas.avatar-pulse {
    animation: avatarLink 0.9s ease-out;
}
@keyframes avatarLink {
    0%   { transform: translateY(0px) scale(0.98); }
    45%  { transform: translateY(-10px) scale(1.05); }
    100% { transform: translateY(0px) scale(1.0); }
}

/* BACKGROUND CANVASES */
#codeCanvas, #ringsCanvas {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
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
/* Make iframe try to match viewport height */
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

const spawnPadding = 40;
let bagX = spawnPadding + Math.random() * (window.innerWidth  - 120 - spawnPadding * 2);
let bagY = spawnPadding + Math.random() * (window.innerHeight - 120 - spawnPadding * 2);
bagNav.style.left = bagX + "px";
bagNav.style.top  = bagY + "px";

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
    bagNav.style.top  = bagY + "px";

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

/* glow when border is hit */
function triggerHitGlow() {
    const target = bagMenu.classList.contains("open") ? bagMenu : bagIcon;
    if (!target) return;
    target.classList.add("bag-hit-glow");
    setTimeout(() => target.classList.remove("bag-hit-glow"), 220);
}

/* FLOATING physics (no gravity, just inertia + bounces) */
function animateBag(){
    const padding = 10;
    if (!draggingBag) {
        bagX += vx;
        bagY += vy;

        const navW = bagNav.offsetWidth || 120;
        const navH = bagNav.offsetHeight || 120;

        let maxX = window.innerWidth  - navW - padding;
        let maxY = window.innerHeight - navH - padding;

        if (bagX < padding) {
            bagX = padding;
            vx = -vx * 0.7;
            triggerHitGlow();
        } else if (bagX > maxX) {
            bagX = maxX;
            vx = -vx * 0.7;
            triggerHitGlow();
        }
        if (bagY < padding) {
            bagY = padding;
            vy = -vy * 0.7;
            triggerHitGlow();
        } else if (bagY > maxY) {
            bagY = maxY;
            vy = -vy * 0.7;
            triggerHitGlow();
        }

        if (bagMenu.classList.contains("open")) {
            const vw = window.innerWidth;
            const menuHalf = (bagMenu.offsetWidth || 200) / 2;
            const bagCenterX = bagX + navW / 2;
            let pushX = 0;

            if (bagCenterX - menuHalf < padding) {
                pushX = padding - (bagCenterX - menuHalf);
            } else if (bagCenterX + menuHalf > vw - padding) {
                pushX = (vw - padding) - (bagCenterX + menuHalf);
            }

            if (pushX !== 0) {
                bagX += pushX;
                vx = -vx * 0.7;
                triggerHitGlow();
            }
        }

        vx *= 0.985;
        vy *= 0.985;

        bagNav.style.left = bagX + "px";
        bagNav.style.top  = bagY + "px";

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
    const chars = "01xyzλΣµσπ∂µσπ{}()[]+-*/<>:=._#";
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

    codeParticles.forEach((p, idx) => {
        codeCtx.font = p.size + "px 'JetBrains Mono', monospace";
        codeCtx.fillStyle = "rgba(255,215,0," + p.alpha + ")";
        codeCtx.fillText(p.token, p.x, p.y);

        p.y += p.speed;
        p.x += p.speed * 0.1;

        if (p.y > codeCanvas.height + 40) {
            p.y = -20;
            p.x = Math.random() * codeCanvas.width;

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

/* ------------------ RINGS – rotating ------------------ */
const rCanvas = document.getElementById("ringsCanvas");
const rctx = rCanvas.getContext("2d");

function animateRings(){
    fitCanvas(rCanvas);
    const w = rCanvas.width, h = rCanvas.height;
    rctx.clearRect(0,0,w,h);

    const cx = w * 0.70;
    const cy = h * 0.64;
    const t  = Date.now() * 0.00010;

    const speeds = [0.8, -0.6, 0.35];

    for (let i=0;i<3;i++){
        const R = 130 + i*40;
        const alpha = 0.38 - i*0.09;

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

/* random entry direction each reload */
if (avatarCanvas) {
    const entryClass = Math.random() < 0.5 ? "avatar-enter-left" : "avatar-enter-right";
    avatarCanvas.classList.add(entryClass);
}

const renderer = new THREE.WebGLRenderer({canvas: avatarCanvas, alpha:true});
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
camera.position.set(0, 1.1, 2.5);

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

let draggingAvatar = false, prevX = 0;
let rot = 0.01;
let avatarActive = false;  // starts rotating only after name decodes

avatarCanvas.addEventListener("mousedown", e => {
    draggingAvatar = true;
    prevX = e.clientX;
});
window.addEventListener("mouseup", () => { draggingAvatar = false; });
window.addEventListener("mousemove", e => {
    if (draggingAvatar && avatar) {
        rot = (e.clientX - prevX) * 0.0004;
        prevX = e.clientX;
    }
});

function animateAvatar(){
    requestAnimationFrame(animateAvatar);
    if (avatar && avatarActive) {
        avatar.rotation.y += rot;
    }
    renderer.setSize(avatarCanvas.clientWidth, avatarCanvas.clientHeight);
    renderer.render(scene, camera);
}
animateAvatar();

/* ------------------ CODED TEXT REVEAL FOR NAME + ROLE ------------------ */
const heroNameEl = document.querySelector('.hero-name');
const heroRoleEl = document.querySelector('.hero-role');
const CODE_CHARS = "01xyzλΣµσπ{}[]<>/\\\\|=_+*#";

function randomCodeStringFromTemplate(template) {
    let out = "";
    for (let i = 0; i < template.length; i++) {
        const ch = template[i];
        if (ch === " ") {
            out += " ";
        } else {
            out += CODE_CHARS[Math.floor(Math.random() * CODE_CHARS.length)];
        }
    }
    return out;
}

function runCodeEffect(el, targetText, totalDurationMs, onDone) {
    if (!el) return;
    const len = targetText.length;
    let idx = 0;
    const interval = totalDurationMs / Math.max(len, 1);

    const timer = setInterval(() => {
        let out = "";
        for (let i = 0; i < len; i++) {
            const ch = targetText[i];
            if (ch === " ") {
                out += " ";
            } else if (i <= idx) {
                out += ch;
            } else {
                out += CODE_CHARS[Math.floor(Math.random() * CODE_CHARS.length)];
            }
        }
        el.textContent = out;
        idx++;
        if (idx >= len) {
            el.textContent = targetText;
            clearInterval(timer);
            if (onDone) onDone();
        }
    }, interval);
}

/* Start both as pure code noise – name "fed by code" */
if (heroNameEl) {
    heroNameEl.textContent = randomCodeStringFromTemplate("Mark Chweya");
}
if (heroRoleEl) {
    heroRoleEl.textContent = randomCodeStringFromTemplate("Data Science & Artificial Intelligence");
}

/* When name finishes: avatar reacts, rotation starts, name sheds code layer */
setTimeout(() => {
    runCodeEffect(
        heroNameEl,
        "Mark Chweya",
        3200,
        () => {
            avatarActive = true;
            const canvasEl = document.getElementById("avatarCanvas");
            if (canvasEl) {
                canvasEl.classList.add("avatar-pulse");
                setTimeout(() => canvasEl.classList.remove("avatar-pulse"), 900);
            }
            if (heroNameEl) {
                heroNameEl.classList.add("decoded");
            }
        }
    );
    runCodeEffect(
        heroRoleEl,
        "Data Science & Artificial Intelligence",
        3600,
        null
    );
}, 750);

/* ------------------ OCCASIONAL NAME SHINE ------------------ */
function triggerShineOnce() {
    if (!heroNameEl) return;
    heroNameEl.classList.add('shine');
    setTimeout(() => {
        heroNameEl.classList.remove('shine');
    }, 3800);
}

setTimeout(() => {
    triggerShineOnce();
    setInterval(() => {
        const extraDelay = Math.random() * 6000;
        setTimeout(triggerShineOnce, extraDelay);
    }, 12000);
}, 4300);

/* STREAMLIT PANEL MESSAGES */
function sendPanel(name){
    window.parent.postMessage({panel: name}, "*");
}
</script>
"""

components.html(hero_html, height=800, scrolling=False)

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
    background:rgba(5,5,8,0.90);
    backdrop-filter:blur(26px);
    transition:0.3s ease;
    z-index:99999999;
    padding:120px;
    color:white;
    box-shadow: 0 0 40px rgba(0,0,0,0.85);
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
    text-shadow:0 0 24px rgba(0,0,0,0.9);
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
