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
# ROUTER USING query_params
# -------------------------------------------------------------
params = st.query_params
if "page" not in params:
    st.query_params["page"] = "Home"

current_page = st.query_params.get("page", "Home")

# -------------------------------------------------------------
# LUXURY BLACK-GOLD THEME + FIXED NAVBAR
# -------------------------------------------------------------
st.markdown("""
<style>

html, body {
    background: #050507;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

/* NAVBAR */
.navbar {
    position: fixed;
    top: 5%;
    left: 50%;
    transform: translateX(-50%);
    width: 75%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 215, 0, 0.25);
    backdrop-filter: blur(20px);
    border-radius: 16px;
    padding: 15px 0px;
    display: flex;
    justify-content: center;
    gap: 45px;
    z-index: 99999;
    box-shadow: 0 0 25px rgba(255,215,0,0.25);
}

/* NAV ITEMS */
.nav-item {
    color: #f6d47a !important;
    font-size: 17px;
    font-weight: 600;
    text-decoration: none;
    transition: 0.3s;
}

.nav-item:hover {
    color: white !important;
    text-shadow: 0 0 12px gold;
}

/* HERO TITLE */
.hero-title {
    font-size: 58px;
    font-weight: 900;
    background: linear-gradient(to right, #f6d47a, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
}

.hero-sub {
    font-size: 24px;
    font-weight: 300;
    margin-top: -10px;
    opacity: 0.85;
    color: #d8d8d8;
}

/* HERO SECTION full screen */
.hero-section {
    height: 100vh;
    width: 100%;
    position: relative;
    overflow: hidden;
    padding-top: 180px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# NAVBAR HTML
# -------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <a href="/?page=Home" class="nav-item">Home</a>
    <a href="/?page=Projects" class="nav-item">Projects</a>
    <a href="/?page=About" class="nav-item">About</a>
    <a href="/?page=Resume" class="nav-item">Resume</a>
    <a href="/?page=Contact" class="nav-item">Contact</a>
</div>
""", unsafe_allow_html=True)
# -------------------------------------------------------------
# HOME PAGE — ONE-SCREEN HERO SECTION
# -------------------------------------------------------------
if current_page == "Home":

    hero_html = """
    <div class="hero-section">

        <!-- Import THREE.js + GLB Loader -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/loaders/GLTFLoader.js"></script>

        <!-- Rising Adinkra Canvas -->
        <canvas id="adinkraUp"
            style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:1;">
        </canvas>

        <!-- Rotating Rings -->
        <canvas id="ringsCanvas"
            style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:2;">
        </canvas>

        <!-- Avatar -->
        <canvas id="avatarCanvas"
            style="position:absolute;left:5%;top:50%;transform:translateY(-50%);
                   width:35%;height:75%;z-index:4;">
        </canvas>

        <!-- TEXT -->
        <div style="position:absolute;right:8%;top:50%;
                    transform:translateY(-50%);z-index:10;text-align:left;">
            <h1 class="hero-title">Mark Chweya</h1>
            <p class="hero-sub">Data Science & AI.</p>
        </div>


    <script>
    // Resize helper
    function fit(canvas){
        const w = canvas.clientWidth, h = canvas.clientHeight;
        if(canvas.width!=w || canvas.height!=h){ canvas.width=w; canvas.height=h; }
    }

    // ============================================================
    // RISING ADINKRA SYMBOLS (light mode)
    // ============================================================
    const upCanvas = document.getElementById("adinkraUp");
    const uctx = upCanvas.getContext("2d");
    const symbols = ["✺","✤","❂"];
    let rise = [];

    function initUp(){
        fit(upCanvas);
        rise = [];
        for(let i=0;i<20;i++){
            rise.push({
                x: Math.random()*upCanvas.width,
                y: Math.random()*upCanvas.height,
                speed: 0.4 + Math.random()*0.8,
                size: 12 + Math.random()*10,
                symbol: symbols[Math.floor(Math.random()*symbols.length)]
            });
        }
    }

    function animateUp(){
        fit(upCanvas);
        uctx.clearRect(0,0,upCanvas.width,upCanvas.height);
        uctx.fillStyle = "rgba(255,215,0,0.85)";
        rise.forEach(s=>{
            uctx.font = s.size+"px serif";
            uctx.fillText(s.symbol,s.x,s.y);
            s.y -= s.speed;
            if(s.y < -20){
                s.y = upCanvas.height+20;
                s.x = Math.random()*upCanvas.width;
            }
        });
        requestAnimationFrame(animateUp);
    }

    initUp();
    animateUp();


    // ============================================================
    // GOLD RINGS
    // ============================================================
    const ringCanvas = document.getElementById("ringsCanvas");
    const rctx = ringCanvas.getContext("2d");

    function animateRings(){
        fit(ringCanvas);
        const w = ringCanvas.width, h = ringCanvas.height;

        rctx.clearRect(0,0,w,h);

        const cx = w*0.22, cy = h*0.50;
        const t = Date.now()*0.00004;

        for(let i=0;i<3;i++){
            const R = 120 + i*36;
            rctx.beginPath();
            rctx.arc(cx,cy,R,0,Math.PI*2);
            rctx.strokeStyle = "rgba(255,215,0,"+(0.45-i*0.1)+")";
            rctx.lineWidth = 3;

            rctx.save();
            rctx.translate(cx,cy);
            rctx.rotate( (i%2==0?1:-1)*t );
            rctx.translate(-cx,-cy);
            rctx.stroke();
            rctx.restore();
        }
        requestAnimationFrame(animateRings);
    }
    animateRings();


    // ============================================================
    // AVATAR (smaller)
    // ============================================================
    const avatarCanvas = document.getElementById("avatarCanvas");
    const renderer = new THREE.WebGLRenderer({canvas:avatarCanvas,alpha:true});
    renderer.setPixelRatio(window.devicePixelRatio);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
    camera.position.set(0,1.1,2.4);

    const key = new THREE.DirectionalLight(0xf6d47a,1.2);
    key.position.set(2,3,4);
    scene.add(key);

    const fill = new THREE.DirectionalLight(0xffffff,0.5);
    fill.position.set(-2,0,3);
    scene.add(fill);

    let avatar = null;
    const loader = new THREE.GLTFLoader();
    loader.load(
        "https://models.readyplayer.me/691a321f28f4be8b0c02cf2e.glb",
        gltf=>{
            avatar = gltf.scene;
            avatar.scale.set(1.6,1.6,1.6);  // smaller avatar
            avatar.position.y = -1.3;
            scene.add(avatar);
        }
    );

    let dragging=false, prevX=0, rotSpeed=0.004;

    avatarCanvas.addEventListener("mousedown",e=>{
        dragging=true; prevX=e.clientX;
    });

    window.addEventListener("mouseup",()=>dragging=false);

    window.addEventListener("mousemove",e=>{
        if(dragging && avatar){
            rotSpeed = (e.clientX-prevX)*0.0005;
            prevX=e.clientX;
        }
    });

    function renderAvatar(){
        requestAnimationFrame(renderAvatar);
        if(avatar) avatar.rotation.y += rotSpeed;
        renderer.setSize(avatarCanvas.clientWidth,avatarCanvas.clientHeight);
        renderer.render(scene,camera);
    }
    renderAvatar();

    </script>

    </div>
    """

    components.html(hero_html, height=900)
# -------------------------------------------------------------
# PROJECTS PAGE
# -------------------------------------------------------------
if current_page == "Projects":
    st.markdown("## 🌟 Projects")

    st.write("""
### 🔹 Titanic Survival Predictor  
Predicts survival probability using ML.  
👉 https://markchweya.shinyapps.io/Titanic-Survival-Rate-Predictor/

### 🔹 AQI Predictor  
Predicts Air Quality Index.  
👉 https://aqi-predictor2.streamlit.app

### 🔹 Mental Health Predictor (USA)  
Predicts likelihood of needing mental health treatment.  
👉 https://mentalhealthpredictorusa.streamlit.app

### 🔹 KukiLabs  
AI Tools & Prototypes.  
👉 https://kukilabs.streamlit.app
    """)


# -------------------------------------------------------------
# ABOUT PAGE
# -------------------------------------------------------------
if current_page == "About":
    st.markdown("## 👨🏾‍💻 About Me")

    st.write("""
I am **Mark Chweya**, a Data Science & Analytics student at USIU–Africa.

I build modern machine learning applications, predictive models, and AI tools
with a futuristic African aesthetic.

I combine:
- Data Science  
- AI Engineering  
- UI Design  
- African Futurism  

to create memorable digital products.
    """)


# -------------------------------------------------------------
# RESUME PAGE
# -------------------------------------------------------------
if current_page == "Resume":
    st.markdown("## 📄 Resume")

    st.write("""
### 🎓 Education  
- USIU–Africa — Data Science & Analytics  
- Moringa School — Software Programming  
- Pioneer School — KCSE  

### 🧠 Skills  
Python • R • SQL • Machine Learning  
Data Visualization • Predictive Analytics  
React • Streamlit  

### 🏅 Certifications  
- Certificate in Computer Programming  

### 🏀 Interests  
Football (Manchester United)  
Basketball (Lakers)  
Golf  

### 📞 Contact  
Email: **chweyamark@gmail.com**  
Phone: **+254 703 951 840**
    """)


# -------------------------------------------------------------
# CONTACT PAGE
# -------------------------------------------------------------
if current_page == "Contact":
    st.markdown("## ✉ Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("Message")

    if st.button("Send Message"):
        st.success("Message sent! (Email integration coming soon.)")
