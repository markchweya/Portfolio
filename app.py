import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------
st.set_page_config(
    page_title="Mark Chweya",
    page_icon="👨🏾‍💻",
    layout="wide"
)

# -------------------------------------------------------------
# SESSION STATE FOR NAVIGATION
# -------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def navigate_to(page_name):
    st.session_state.page = page_name

# -------------------------------------------------------------
# HANDLE NAVIGATION USING NEW Streamlit PARAMS API
# -------------------------------------------------------------
params = st.query_params
if "page" in params:
    st.session_state.page = params["page"]

# -------------------------------------------------------------
# GLOBAL BLACK × GOLD LUXURY THEME + FLOATING NAVBAR CSS
# -------------------------------------------------------------
st.markdown("""
<style>

html, body {
    margin: 0;
    padding: 0;
    background: #000000;
    color: #f2f2f2;
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
}

/* ---------------- FLOATING GLASS NAVBAR ---------------- */

.navbar {
    position: fixed;
    top: 5%;
    left: 50%;
    transform: translateX(-50%);
    width: 75%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 215, 0, 0.25);
    backdrop-filter: blur(18px);
    border-radius: 14px;
    padding: 18px 28px;
    display: flex;
    justify-content: center;
    gap: 38px;
    z-index: 99999;
    box-shadow: 0 0 25px rgba(255,215,0,0.25);
}

.nav-item {
    color: #f6d47a;
    font-weight: 500;
    font-size: 17px;
    cursor: pointer;
    transition: 0.3s;
}

.nav-item:hover {
    color: #ffffff;
    text-shadow: 0 0 10px gold;
}

/* ---------------- BASIC LAYOUT / HERO ---------------- */

.section {
    padding: 140px 60px;
}

.hero-text-title {
    font-size: 62px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
}

.hero-text-sub {
    font-size: 26px;
    font-weight: 300;
    opacity: 0.85;
}

@media (max-width: 980px) {
    .hero-row {
        flex-direction: column;
        text-align: center;
    }
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# FLOATING NAVBAR HTML
# -------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <span class="nav-item" onclick="window.location.href='/?page=Home'">Home</span>
    <span class="nav-item" onclick="window.location.href='/?page=Projects'">Projects</span>
    <span class="nav-item" onclick="window.location.href='/?page=About'">About</span>
    <span class="nav-item" onclick="window.location.href='/?page=Resume'">Resume</span>
    <span class="nav-item" onclick="window.location.href='/?page=Contact'">Contact</span>
</div>
""", unsafe_allow_html=True)
# -------------------------------------------------------------
# HOME PAGE (Hero + Avatar + Rings + Gold Dust + Adinkra Rain)
# -------------------------------------------------------------
if st.session_state.page == "Home":

    st.markdown("<div class='section'>", unsafe_allow_html=True)

    hero_html = """
    <div style="position: relative; width: 100%; height: 650px;">

        <!-- THREE.JS LIBRARIES (CRITICAL!) -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>

        <!-- ADINKRA GOLD RAIN -->
        <canvas id="adinkraCanvas"
            style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:1;">
        </canvas>

        <!-- GOLD RINGS -->
        <canvas id="ringsCanvas"
            style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:2;">
        </canvas>

        <!-- AVATAR CANVAS (LEFT SIDE) -->
        <div style="position:absolute;
                    left:4%;
                    top:50%;
                    transform: translateY(-50%);
                    width:40%;
                    height:100%;
                    z-index:5;">
            <canvas id="avatarCanvas" style="width:100%; height:100%;"></canvas>
        </div>

        <!-- HERO TEXT -->
        <div style="position:absolute;
                    right:6%;
                    top:50%;
                    transform: translateY(-50%);
                    width:40%;
                    z-index:10;">
            <h1 class="hero-text-title">Mark Chweya</h1>
            <p class="hero-text-sub">Data Science & AI.</p>
        </div>

        <!-- GOLD DUST -->
        <canvas id="dustCanvas"
            style="position:absolute;
                   bottom:0;
                   left:0;
                   width:100%;
                   height:250px;
                   z-index:3;">
        </canvas>


    <script>
    // ============================================================
    // UTILITY — Ensure canvases match screen size
    // ============================================================
    function resizeCanvasToDisplaySize(canvas) {
        const w = canvas.clientWidth;
        const h = canvas.clientHeight;
        if (canvas.width !== w || canvas.height !== h) {
            canvas.width = w;
            canvas.height = h;
        }
    }

    // ============================================================
    // 1) ADINKRA GOLD RAIN
    // ============================================================
    const adinkraCanvas = document.getElementById("adinkraCanvas");
    const actx = adinkraCanvas.getContext("2d");
    const symbols = ["✺","✤","❂"];
    let drops = [];

    function initAdinkra() {
        resizeCanvasToDisplaySize(adinkraCanvas);
        drops = [];
        for (let i=0; i<60; i++) {
            drops.push({
                x: Math.random()*adinkraCanvas.width,
                y: Math.random()*adinkraCanvas.height,
                speed: 1 + Math.random()*2,
                size: 18 + Math.random()*18,
                symbol: symbols[Math.floor(Math.random()*symbols.length)]
            });
        }
    }

    function animateAdinkra() {
        resizeCanvasToDisplaySize(adinkraCanvas);
        actx.clearRect(0,0,adinkraCanvas.width,adinkraCanvas.height);
        actx.fillStyle = "rgba(255,215,0,0.85)";

        drops.forEach(d => {
            actx.font = d.size + "px serif";
            actx.fillText(d.symbol, d.x, d.y);
            d.y += d.speed;
            if (d.y > adinkraCanvas.height) {
                d.y = -20;
                d.x = Math.random()*adinkraCanvas.width;
            }
        });

        requestAnimationFrame(animateAdinkra);
    }

    initAdinkra();
    animateAdinkra();

    // ============================================================
    // 2) GOLD RINGS
    // ============================================================
    const ringsCanvas = document.getElementById("ringsCanvas");
    const rctx = ringsCanvas.getContext("2d");

    function animateRings() {
        resizeCanvasToDisplaySize(ringsCanvas);
        let w = ringsCanvas.width;
        let h = ringsCanvas.height;

        rctx.clearRect(0,0,w,h);

        let cx = w * 0.22;
        let cy = h * 0.50;

        let t = Date.now() * 0.00004;

        for (let i=0; i<3; i++) {
            let radius = 140 + i*40;
            rctx.beginPath();
            rctx.arc(cx, cy, radius, 0, Math.PI*2);
            rctx.strokeStyle = "rgba(255,215,0," + (0.45 - i*0.1) + ")";
            rctx.lineWidth = 3;

            rctx.save();
            rctx.translate(cx,cy);
            rctx.rotate((i%2===0 ? 1 : -1)*t);
            rctx.translate(-cx,-cy);
            rctx.stroke();
            rctx.restore();
        }

        requestAnimationFrame(animateRings);
    }
    animateRings();

    // ============================================================
    // 3) GOLD DUST
    // ============================================================
    const dustCanvas = document.getElementById("dustCanvas");
    const dctx = dustCanvas.getContext("2d");

    let dust = [];
    for (let i=0; i<70; i++) {
        dust.push({
            x: 60 + Math.random()*380,
            y: 100 + Math.random()*100,
            speed: 0.3 + Math.random()*0.6,
            size: 2 + Math.random()*4
        });
    }

    function animateDust() {
        resizeCanvasToDisplaySize(dustCanvas);
        dctx.clearRect(0,0,dustCanvas.width,dustCanvas.height);

        dctx.fillStyle = "rgba(255,215,0,0.9)";
        dust.forEach(p => {
            dctx.beginPath();
            dctx.arc(p.x, p.y, p.size, 0, Math.PI*2);
            dctx.fill();
            p.y -= p.speed;
            if (p.y < 0) {
                p.y = dustCanvas.height;
                p.x = 60 + Math.random()*380;
            }
        });

        requestAnimationFrame(animateDust);
    }
    animateDust();

    // ============================================================
    // 4) THREE.JS AVATAR (auto-rotate + drag control)
    // ============================================================
    const avatarCanvas = document.getElementById("avatarCanvas");

    const renderer = new THREE.WebGLRenderer({ canvas: avatarCanvas, alpha:true });
    renderer.setPixelRatio(window.devicePixelRatio);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
    camera.position.set(0,1.2,2.8);

    // LIGHTING
    const keyLight = new THREE.DirectionalLight(0xf6d47a, 1.4);
    keyLight.position.set(2,3,4);
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0xffffff, 0.5);
    fillLight.position.set(-2,0,3);
    scene.add(fillLight);

    // LOAD AVATAR
    let avatarModel = null;
    const loader = new THREE.GLTFLoader();
    loader.load(
        "https://models.readyplayer.me/691a321f28f4be8b0c02cf2e.glb",
        gltf => {
            avatarModel = gltf.scene;
            avatarModel.scale.set(2.1,2.1,2.1);
            avatarModel.position.y = -1.45;
            scene.add(avatarModel);
        }
    );

    let isDragging = false;
    let prevX = 0;
    let rotationSpeed = 0.004;

    avatarCanvas.addEventListener("mousedown", e => {
        isDragging = true;
        prevX = e.clientX;
    });

    window.addEventListener("mouseup", ()=> isDragging=false);

    window.addEventListener("mousemove", e => {
        if (isDragging && avatarModel) {
            rotationSpeed = (e.clientX - prevX) * 0.0005;
            prevX = e.clientX;
        }
    });

    function animateAvatar() {
        requestAnimationFrame(animateAvatar);
        if (avatarModel) avatarModel.rotation.y += rotationSpeed;

        renderer.setSize(avatarCanvas.clientWidth, avatarCanvas.clientHeight);
        renderer.render(scene, camera);
    }
    animateAvatar();

    </script>
    """

    components.html(hero_html, height=700)
    st.markdown("</div>", unsafe_allow_html=True)
# -------------------------------------------------------------
# PROJECTS PAGE
# -------------------------------------------------------------
if st.session_state.page == "Projects":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("## 🌟 Projects")

    st.markdown("""
    <style>
    .project-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,215,0,0.25);
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 18px;
        box-shadow: 0 0 15px rgba(255,215,0,0.15);
        transition: 0.3s;
    }
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 0 25px rgba(255,215,0,0.45);
    }
    a {
        color: #f6d47a;
        text-decoration: none;
    }
    a:hover {
        text-shadow: 0 0 10px gold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <h3>Titanic Survival Predictor</h3>
        <p>Machine learning survival prediction model.</p>
        <a href="https://markchweya.shinyapps.io/Titanic-Survival-Rate-Predictor/" target="_blank">
            View Project
        </a>
    </div>

    <div class="project-card">
        <h3>AQI Predictor</h3>
        <p>Predict air quality index levels with ML.</p>
        <a href="https://aqi-predictor2.streamlit.app" target="_blank">
            View Project
        </a>
    </div>

    <div class="project-card">
        <h3>Mental Health Predictor (USA)</h3>
        <p>Predict need for mental health treatment.</p>
        <a href="https://mentalhealthpredictorusa.streamlit.app" target="_blank">
            View Project
        </a>
    </div>

    <div class="project-card">
        <h3>KukiLabs AI</h3>
        <p>AI tools & experimental ML apps.</p>
        <a href="https://kukilabs.streamlit.app" target="_blank">
            Explore
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------------------
# ABOUT PAGE
# -------------------------------------------------------------
if st.session_state.page == "About":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("## 👨🏾‍💻 About Me")

    st.write("""
I am **Mark Chweya**, Data Science & Analytics student at USIU–Africa.

I build:
- Machine learning applications  
- Predictive models  
- Interactive AI tools  
- Modern, futuristic tech experiences  

I'm passionate about blending **African futurism** with **cutting-edge AI** to create unique and impactful digital products.
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------------------
# RESUME PAGE
# -------------------------------------------------------------
if st.session_state.page == "Resume":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("## 📄 Resume")

    st.write("""
### 🎓 Education  
- USIU–Africa — Data Science & Analytics  
- Moringa School — Software Programming  
- Pioneer School — KCSE  

### 🛠 Skills  
Python, R, SQL  
Machine Learning  
Data Science  
React / JavaScript  
Streamlit  
Predictive Modeling  

### 🏅 Certifications  
- Certificate in Computer Programming  

### 🏀 Interests  
Football (Manchester United)  
Basketball (Lakers)  
Golf  

### 📞 Contact  
- Email: **chweyamark@gmail.com**  
- Phone: **+254 703 951 840**
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------------------
# CONTACT PAGE
# -------------------------------------------------------------
if st.session_state.page == "Contact":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("## ✉ Contact Me")

    st.markdown("""
        <style>
        .contact-box {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,215,0,0.25);
            padding: 30px;
            border-radius: 16px;
            width: 60%;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 0 20px rgba(255,215,0,0.25);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='contact-box'>", unsafe_allow_html=True)

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("Message")

    if st.button("Send Message"):
        st.success("Message sent! (Email integration coming soon.)")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
