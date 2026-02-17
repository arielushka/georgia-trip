import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- הגדרות עיצוב ותוכן ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Roadmap</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-main: #0b1120;       /* רקע כהה מאוד */
            --card-bg: #1e293b;       /* רקע כרטיסים */
            --text-bright: #ffffff;   /* טקסט לבן בוהק */
            --text-dim: #94a3b8;      /* טקסט אפור משני */
            --accent: #38bdf8;        /* תכלת סייבר */
            --danger: #ef4444;        /* אדום להתקפה */
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-bright);
            font-family: 'Rubik', sans-serif;
            overflow-x: hidden;
        }

        /* ניווט */
        .navbar {
            background-color: #151e32 !important;
            border-bottom: 1px solid #334155;
            padding: 15px 0;
        }
        .navbar-brand { font-weight: 800; color: var(--accent) !important; letter-spacing: 1px; }
        .nav-link { color: var(--text-dim) !important; font-weight: 500; margin-left: 20px; transition: 0.3s; }
        .nav-link:hover, .nav-link.active { color: var(--text-bright) !important; }

        /* כותרות */
        .hero-section {
            padding: 70px 0;
            text-align: center;
            background: radial-gradient(circle at top, #1e293b 0%, var(--bg-main) 70%);
            border-bottom: 1px solid #1e293b;
            margin-bottom: 40px;
        }
        .display-4 { font-weight: 800; letter-spacing: -1px; text-shadow: 0 0 20px rgba(56, 189, 248, 0.3); }
        .lead { color: var(--text-dim); max-width: 700px; margin: 0 auto; }

        /* כרטיסים */
        .cyber-card {
            background-color: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 12px;
            margin-bottom: 20px;
            overflow: hidden;
            transition: transform 0.2s, border-color 0.2s;
        }
        .cyber-card:hover {
            transform: translateY(-2px);
            border-color: var(--accent);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        /* עיצוב פנימי */
        .card-header-custom {
            padding: 20px;
            display: flex;
            align-items: center;
            cursor: pointer;
            background: rgba(255,255,255,0.02);
        }
        .icon-wrap {
            width: 45px; height: 45px;
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.2rem;
            margin-left: 15px;
            background: rgba(255,255,255,0.05);
        }
        .course-details {
            padding: 25px;
            border-top: 1px solid #334155;
            background: #182235;
        }

        /* כפתורים */
        .btn-glow {
            display: block;
            width: 100%;
            padding: 12px;
            text-align: center;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            transition: 0.3s;
            margin-top: 20px;
        }
        .btn-cisco { border: 2px solid var(--accent); color: var(--accent); }
        .btn-cisco:hover { background: var(--accent); color: white; box-shadow: 0 0 20px rgba(56, 189, 248, 0.4); }
        
        .btn-hack { background: var(--danger); color: white; border: none; }
        .btn-hack:hover { background: #dc2626; color: white; box-shadow: 0 0 20px rgba(239, 68, 68, 0.4); }

        /* כללי */
        ul { color: var(--text-dim); }
        li { margin-bottom: 8px; }
        strong { color: var(--text-bright); }
        .video-box {
            position: relative; padding-bottom: 56.25%; height: 0;
            border-radius: 8px; overflow: hidden; margin-top: 15px;
            border: 1px solid #334155;
        }
        .video-box iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }

    </style>
</head>
<body>

    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/"><i class="fas fa-terminal me-2"></i>CYBER<span class="text-white">ROADMAP</span></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="nav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link {% if mode=='courses' %}active{% endif %}" href="/">קורסים</a></li>
                    <li class="nav-item"><a class="nav-link {% if mode=='practice' %}active{% endif %}" href="/practice">תרגול מעשי</a></li>
                </ul>
            </div>
        </div>
    </nav>

    {% if mode == 'courses' %}
    <div class="hero-section">
        <div class="container">
            <h1 class="display-4 mb-3">מסלול הלימוד</h1>
            <p class="lead">הקורסים הרשמיים של Cisco (NetAcad) בסדר הנכון.<br>אל תדלג על שלבים - הבסיס הוא הכל.</p>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                {% for c in courses %}
                <div class="cyber-card" data-bs-toggle="collapse" data-bs-target="#c{{ c.id }}">
                    <div class="card-header-custom">
                        <span class="h3 mb-0 text-muted ms-3 opacity-25">0{{ c.id }}</span>
                        <div class="icon-wrap" style="color:{{c.color}}; border:1px solid {{c.color}}"><i class="fas {{c.icon}}"></i></div>
                        <div class="flex-grow-1">
                            <h5 class="mb-1 fw-bold">{{ c.title }}</h5>
                            <span class="badge bg-dark border border-secondary">{{ c.duration }}</span>
                        </div>
                        <i class="fas fa-chevron-down text-muted"></i>
                    </div>
                    <div class="collapse" id="c{{ c.id }}">
                        <div class="course-details">
                            <h6 class="text-info mb-2">על הקורס</h6>
                            <p class="text-muted small mb-4">{{ c.desc }}</p>
                            <h6 class="text-info mb-2">מה לומדים?</h6>
                            <ul class="small ps-3">
                                {% for s in c.syllabus %}<li>{{ s }}</li>{% endfor %}
                            </ul>
                            <a href="https://www.netacad.com/catalogs/learn" target="_blank" class="btn-glow btn-cisco">
                                לקטלוג הקורסים <i class="fas fa-external-link-alt ms-2"></i>
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>

    {% elif mode == 'practice' %}
    <div class="hero-section">
        <div class="container">
            <h1 class="display-4 mb-3">אזור התרגול</h1>
            <p class="lead">סיימת את התיאוריה? זה הזמן להפשיל שרוולים.<br>מומלץ להתחיל כאן רק לאחר סיום 'Networking Essentials'.</p>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row g-4 justify-content-center">
            <div class="col-lg-5">
                <div class="cyber-card h-100 p-4 text-center">
                    <i class="fas fa-flag-checkered fa-3x text-white mb-3"></i>
                    <h3 class="fw-bold">picoCTF</h3>
                    <p class="text-muted small">פתרון חידות סייבר בסגנון "Capture The Flag". מצוין למתחילים.</p>
                    <div class="video-box">
                        <iframe src="https://www.youtube.com/embed/videoseries?list=PL1H1sFpDiRzZ6Hk4R9Y5e3_wWz3_wWz3" allowfullscreen></iframe>
                    </div>
                    <a href="https://picoctf.org/" target="_blank" class="btn-glow btn-hack">התחל לשחק</a>
                </div>
            </div>
            <div class="col-lg-5">
                <div class="cyber-card h-100 p-4 text-center">
                    <i class="fas fa-cube fa-3x text-white mb-3"></i>
                    <h3 class="fw-bold">TryHackMe</h3>
                    <p class="text-muted small">מעבדות וירטואליות מודרכות. תוקפים מכונות אמיתיות דרך הדפדפן.</p>
                    <div class="video-box">
                        <iframe src="https://www.youtube.com/embed/fNZdXq2jXWU" allowfullscreen></iframe>
                    </div>
                    <a href="https://tryhackme.com/" target="_blank" class="btn-glow btn-hack">פתח חשבון</a>
                </div>
            </div>
        </div>
    </div>
    {% endif %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

courses_data = [
    {"id": 1, "title": "Networking Basics", "duration": "25 שעות", "color": "#38bdf8", "icon": "fa-wifi", "desc": "היסודות. לומדים על כתובות IP, סוגי רשתות ואיך האינטרנט עובד פיזית.", "syllabus": ["כתובות IP ו-MAC", "רכיבי תקשורת (Router/Switch)", "LAN vs WAN"]},
    {"id": 2, "title": "Packet Tracer", "duration": "10 שעות", "color": "#818cf8", "icon": "fa-laptop-code", "desc": "סימולטור הרשתות. לומדים לבנות רשתות וירטואליות לפני שנוגעים בציוד אמיתי.", "syllabus": ["התקנה והכרת הממשק", "בניית רשת פשוטה", "בדיקת תקשורת (Ping)"]},
    {"id": 3, "title": "Networking Essentials", "duration": "70 שעות", "color": "#c084fc", "icon": "fa-network-wired", "desc": "קורס הליבה. צוללים למודל ה-OSI ולפרוטוקולים. זה הבסיס הקריטי ביותר להאקרים.", "syllabus": ["מודל 7 השכבות", "פרוטוקולי TCP/UDP", "אבטחת מידע בסיסית"]},
    {"id": 4, "title": "Intro to Cybersecurity", "duration": "15 שעות", "color": "#f472b6", "icon": "fa-shield-alt", "desc": "מבוא לאבטחה. מי התוקפים? מה הם רוצים? ואיך מגנים על ארגון?", "syllabus": ["הנדסה חברתית", "סוגי נוזקות (Malware)", "עקרונות CIA"]},
    {"id": 5, "title": "Linux Unhatched", "duration": "8 שעות", "color": "#fbbf24", "icon": "fa-terminal", "desc": "מערכת ההפעלה של הסייבר. לומדים לעבוד עם הטרמינל (שורת הפקודה).", "syllabus": ["פקודות בסיסיות", "ניהול קבצים", "הרשאות"]}
]

@app.route('/')
def home(): return render_template_string(HTML_TEMPLATE, mode='courses', courses=courses_data)

@app.route('/practice')
def practice(): return render_template_string(HTML_TEMPLATE, mode='practice')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
