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
# REMOVE STREAMLIT DEFAULTS
# --------------------------------------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
html, body {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# HERO SECTION HTML (LAYOUT A)
# --------------------------------------------------------
hero_html = """
<style>

html, body {
    overflow: hidden !important;
    margin: 0;
    padding: 0;
}

/* HERO FULLSCREEN */
.hero-wrap {
    position: fixed;
    top: 0;
    left: 0;

    width: 100vw;
    height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    gap: 140px;
    z-index: 1;
}

/* NAVBAR */
.navbar {
    position: absolute;
    top: 25px;
    left: 50%;
    transform: translateX(-50%);

    display: flex;
    gap: 40px;

    padding: 12px 40px;

    background: rgba(20,20,20,0.55);
    border: 1px solid rgba(255,215,0,0.4);
    border-radius: 18px;
    backdrop-filter: blur(22px);

    z-index: 999999999;
}

.nav-item {
    font-size: 20px;
    font-weight: 600;
    color: #f6d47a;
    cursor: pointer;
}
.nav-item:hover {
    color: white;
    text-shadow: 0 0 12px gold;
}

/* NAME SECTION */
.hero-left {
    display: flex;
    flex-direction: column;
    justify-content: center;
    transform: translateY(-20px);
}

.hero-name {
    font-size: 74px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
}
.hero-role {
    font-size: 30px;
    color: #eaeaea;
    margin-top: -12px;
}

/* AVATAR CANVAS */
#avatarCanvas {
    width: 400px;
    height: 550px;

    transform: translateY(-20px);
    z-index: 5;
}

/* RINGS */
#ringsCanvas {
    position:absolute;
    left:0;
    top:0;
    width:100%;
    height:100%;
    z-index:0;
}

/* ADINKRA SYMBOLS */
#adinkraCanvas {
    position:absolute;
    left:0;
    top:0;
    width:100%;
    height:100%;
    z-index:0;
}

</style>

<div class="hero-wrap">

    <div class="navbar">
        <span class="nav-item" onclick="sendPanel('Home')">Home</span>
        <span class="nav-item" onclick="sendPanel('Projects')">Projects</span>
        <span class="nav-item" onclick="sendPanel('About')">About</span>
        <span class="nav-item" onclick="sendPanel('Resume')">Resume</span>
        <span class="nav-item" onclick="sendPanel('Contact')">Contact</span>
    </div>

    <!-- Rising Adinkra -->
    <canvas id="adinkraCanvas"></canvas>

    <!-- Rings -->
    <canvas id="ringsCanvas"></canvas>

    <!-- Left: Name -->
    <div class="hero-left">
        <div class="hero-name">Mark Chweya</div>
        <div class="hero-role">Data Science & Artificial Intelligence</div>
    </div>

    <!-- Right: Avatar -->
    <canvas id="avatarCanvas"></canvas>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>

<script>

/* ========== CANVAS FITTER ========== */
function fitCanvas(c){
    const w = c.clientWidth, h = c.clientHeight;
    if(c.width != w || c.height != h){
        c.width = w; c.height = h;
    }
}

/* ========== ADINKRA SYMBOLS ========== */
const aCanvas = document.getElementById("adinkraCanvas");
const actx = aCanvas.getContext("2d");
const symbols = ["✺","✤","❂"];
let adinkra = [];

function initAdinkra(){
    fitCanvas(aCanvas);
    adinkra = [];
    for(let i=0;i<25;i++){
        adinkra.push({
            x: Math.random()*aCanvas.width,
            y: Math.random()*aCanvas.height,
            size: 10 + Math.random()*8,
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
        actx.font = s.size+"px serif";
        actx.fillText(s.char, s.x, s.y);
        s.y -= s.speed;
        if(s.y < -20){ s.y = aCanvas.height+20; s.x = Math.random()*aCanvas.width; }
    });
    requestAnimationFrame(animateAdinkra);
}
initAdinkra();
animateAdinkra();

/* ========== RINGS ========== */
const rCanvas = document.getElementById("ringsCanvas");
const rctx = rCanvas.getContext("2d");

function animateRings(){
    fitCanvas(rCanvas);
    const w=rCanvas.width, h=rCanvas.height;
    rctx.clearRect(0,0,w,h);
    const cx = w*0.72, cy = h*0.50;
    const t = Date.now()*0.00005;

    for(let i=0;i<3;i++){
        const R = 130 + i*40;
        rctx.beginPath();
        rctx.arc(cx,cy,R,0,Math.PI*2);
        rctx.strokeStyle = "rgba(255,215,0,"+(0.35-i*0.1)+")";
        rctx.lineWidth=3;

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

/* ========== AVATAR ========== */
const avatarCanvas = document.getElementById("avatarCanvas");
const renderer = new THREE.WebGLRenderer({canvas: avatarCanvas, alpha:true});
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
camera.position.set(0,1.1,2.3);

/* LIGHTS */
const key = new THREE.DirectionalLight(0xf6d47a,1.2);
key.position.set(2,3,4);
scene.add(key);
scene.add(new THREE.AmbientLight(0xffffff,0.4));

let avatar = null;
const loader = new THREE.GLTFLoader();

loader.load(
    "https://models.readyplayer.me/691a48795f9f523e503e7810.glb",
    gltf=>{
        avatar = gltf.scene;
        avatar.scale.set(1.55,1.55,1.55);
        avatar.position.y = -1.18;
        scene.add(avatar);
    }
);

/* DRAG ROTATION */
let drag=false, prev=0, rot=0.004;
avatarCanvas.addEventListener("mousedown",e=>{drag=true; prev=e.clientX;});
window.addEventListener("mouseup",()=>drag=false);
window.addEventListener("mousemove",e=>{
    if(drag && avatar){
        rot = (e.clientX-prev)*0.0004;
        prev = e.clientX;
    }
});

/* LOOP */
function animateAvatar(){
    requestAnimationFrame(animateAvatar);
    if(avatar) avatar.rotation.y += rot;
    renderer.setSize(avatarCanvas.clientWidth, avatarCanvas.clientHeight);
    renderer.render(scene,camera);
}
animateAvatar();

/* NAV → STREAMLIT */
function sendPanel(p){
    window.parent.postMessage({"panel": p}, "*");
}

</script>
"""

components.html(hero_html, height=1080)

# --------------------------------------------------------
# SLIDING PANELS
# --------------------------------------------------------
panel_engine = """
<style>
.panel {
    position: fixed;
    top: 0;
    left: 100vw;
    width: 100vw;
    height: 100vh;
    background: rgba(10,10,10,0.85);
    backdrop-filter: blur(20px);
    transition: 0.3s ease;
    z-index: 99999999;
    padding: 120px;
    color: white;
}
.panel.active { left: 0; }
.close-btn {
    position:absolute;
    top:40px; right:40px;
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
.panel-body { font-size:20px; width:60%; }
</style>

<div id="panel" class="panel">
    <div class="close-btn" onclick="closePanel()">×</div>
    <div id="panelContent"></div>
</div>

<script>
window.addEventListener("message", event=>{
    if(event.data.panel){
        openPanel(event.data.panel);
    }
});

function openPanel(name){
    fetch("/panel?name="+name)
        .then(r=>r.text())
        .then(html=>{
            document.getElementById("panelContent").innerHTML = html;
            document.getElementById("panel").classList.add("active");
        });
}
function closePanel(){
    document.getElementById("panel").classList.remove("active");
}
</script>
"""
components.html(panel_engine, height=0)

# --------------------------------------------------------
# PANEL CONTENT
# --------------------------------------------------------
def panel_html(title, body):
    return f"""
    <div class="panel-title">{title}</div>
    <div class="panel-body">{body}</div>
    """

panels = {
    "Projects": panel_html("Projects", """
        <p><b>🔹 Titanic Survival Predictor</b><br>
        ML model predicting Titanic survival.</p>

        <p><b>🔹 AQI Predictor</b><br>
        Predicting Air Quality Index.</p>

        <p><b>🔹 Mental Health Predictor</b><br>
        Probability of needing treatment.</p>

        <p><b>🔹 KukiLabs</b><br>
        A collection of AI tools.</p>
    """),

    "About": panel_html("About Me", """
        I am <b>Mark Chweya</b>, a Data Science & AI student at USIU–Africa.<br><br>
        I specialize in ML, AI systems, interactive tools & futuristic African UI.
    """),

    "Resume": panel_html("Resume", """
        <b>Education</b><br>
        • USIU–Africa — Data Science<br>
        • Moringa — Software Engineering<br><br>

        <b>Skills</b><br>
        Python, ML, Streamlit, Data Viz, AI.
    """),

    "Contact": panel_html("Contact Me", """
        Email: <span style='color:#f6d47a;'>chweyamark@gmail.com</span><br>
        Phone: <span style='color:#f6d47a;'>+254 703 951 840</span>
    """)
}

# --------------------------------------------------------
# PANEL ROUTE
# --------------------------------------------------------
name = st.query_params.get("name", None)
if name in panels:
    st.markdown(panels[name], unsafe_allow_html=True)
