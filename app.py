import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- תבנית ה-HTML וה-CSS ---
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
            --bg-dark: #0f172a;
            --card-bg: #1e293b;
            --text-white: #ffffff;
            --text-gray: #cbd5e1;
            --accent: #38bdf8;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-white);
            font-family: 'Rubik', sans-serif;
            overflow-x: hidden;
        }

        /* --- Navbar --- */
        .navbar {
            background-color: #1e293b !important;
            border-bottom: 1px solid #334155;
        }
        .nav-link {
            color: var(--text-gray) !important;
            font-weight: 600;
            margin-left: 15px;
            font-size: 1.1rem;
        }
        .nav-link.active {
            color: var(--accent) !important;
            border-bottom: 2px solid var(--accent);
        }

        /* --- Hero Section --- */
        .hero-section {
            padding: 60px 0;
            text-align: center;
            background: radial-gradient(circle at center, #1e293b 0%, #0f172a 70%);
            border-bottom: 1px solid #334155;
            margin-bottom: 40px;
        }

        .hero-title {
            font-weight: 800;
            background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* --- Cards --- */
        .custom-card {
            background-color: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 16px;
            margin-bottom: 20px;
            transition: 0.3s;
            color: var(--text-white);
        }
        
        .custom-card:hover {
            border-color: var(--accent);
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
        }

        .course-header {
            padding: 20px;
            display: flex;
            align-items: center;
            cursor: pointer;
        }

        .icon-box {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            background: rgba(255,255,255,0.05);
            margin-left: 20px;
        }

        .course-details {
            background: rgba(0,0,0,0.3);
            border-top: 1px solid #334155;
            padding: 30px;
        }

        .practice-container {
            padding: 30px;
        }
        
        .video-wrapper {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            margin-top: 20px;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid #475569;
        }
        .video-wrapper iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        h1, h2, h3, h4, h5, h6 { color: var(--text-white) !important; }
        p, li { color: var(--text-gray); }
        .text-white-force { color: white !important; }

        .btn-action {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }
        .btn-cisco { border: 2px solid var(--accent); color: var(--accent); }
        .btn-cisco:hover { background: var(--accent); color: white; }
        
        .btn-practice { background: #ef4444; color: white; border: none; }
        .btn-practice:hover { background: #dc2626; color: white; box-shadow: 0 0 15px rgba(239,68,68,0.4); }

    </style>
</head>
<body>

    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/"><i class="fas fa-user-secret me-2"></i>CyberRoadmap</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link {% if mode == 'courses' %}active{% endif %}" href="/">
                            <i class="fas fa-book-open ms-1"></i> מסלול הלימוד
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {% if mode == 'practice' %}active{% endif %}" href="/practice">
                            <i class="fas fa-dumbbell ms-1"></i> אזור תרגול
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    {% if mode == 'courses' %}
    <div class="hero-section">
        <div class="container">
            <h1 class="display-4 hero-title">מסלול הלימוד המלא</h1>
            <div class="row justify-content-center mt-3">
                <div class="col-lg-8">
                    <p class="lead text-white-force">
                        ברוכים הבאים! הקורסים המוצגים למטה לקוחים מתוך האקדמיה של <strong>Cisco (NetAcad)</strong>.
                        <br>
                        המסלול בנוי בצורה מדורגת – חשוב מאוד להתקדם שלב אחר שלב.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row justify-content-center">
            <div class="col-lg-9">
                {% for course in courses %}
                <div class="custom-card course-card" data-bs-toggle="collapse" data-bs-target="#c{{ course.id }}">
                    <div class="course-header">
                        <span class="h2 ms-3 mb-0 opacity-50">{{ course.id }}</span>
                        <div class="icon-box" style="color: {{ course.color }}; border: 1px solid {{ course.color }}">
                            <i class="fas {{ course.icon }}"></i>
                        </div>
                        <div class="flex-grow-1">
                            <h4 class="mb-1 fw-bold">{{ course.title }}</h4>
                            <span class="badge bg-secondary">{{ course.duration }}</span>
                        </div>
                        <i class="fas fa-chevron-down opacity-50"></i>
                    </div>

                    <div class="collapse" id="c{{ course.id }}">
                        <div class="course-details">
                            <h5 class="text-accent mb-3"><i class="fas fa-info-circle ms-2"></i>על הקורס</h5>
                            <p>{{ course.desc }}</p>
                            
                            <h5 class="text-accent mb-3 mt-4"><i class="fas fa-list ms-2"></i>מה לומדים?</h5>
                            <ul>
                                {% for item in course.syllabus %}
                                <li>{{ item }}</li>
                                {% endfor %}
                            </ul>
                            
                            <a href="{{ cisco_url }}" target="_blank" class="btn-action btn-cisco w-100 text-center mt-4">
                                עבור לקורס באתר סיסקו <i class="fas fa-external-link-alt ms-2"></i>
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
            <h1 class="display-4 hero-title">אזור התרגול המעשי</h1>
            <p class="lead text-white-force">
                סיימת את התיאוריה? זה הזמן ללכלך את הידיים.
                <br>
                מומלץ להתחיל כאן רק אחרי שסיימת את שלב הרשתות (Networking Essentials).
            </p>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row g-4">
            <div class="col-lg-6">
                <div class="custom-card h-100 practice-container">
                    <div class="text-center mb-4">
                        <i class="fas fa-flag-checkered fa-4x text-white-force mb-3"></i>
                        <h2 class="fw-bold">picoCTF</h2>
                        <p class="text-gray">המקום הכי טוב להתחיל בו משחקי Capture The Flag.</p>
                    </div>
                    <div class="alert alert-dark border-secondary">
                        <small class="text-white-force"><strong>מה עושים שם?</strong> פותרים חידות סייבר (Forensics, Web, Crypto).</small>
                    </div>
                    <h5 class="mt-4 mb-2 text-white-force">מדריך וידאו (John Hammond):</h5>
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/videoseries?list=PL1H1sFpDiRzZ6Hk4R9Y5e3_wWz3_wWz3" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <a href="https://picoctf.org/" target="_blank" class="btn-action btn-practice w-100 text-center mt-4">
                        התחל לשחק ב-picoCTF <i class="fas fa-arrow-left ms-2"></i>
                    </a>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="custom-card h-100 practice-container">
                    <div class="text-center mb-4">
                        <i class="fas fa-cube fa-4x text-white-force mb-3"></i>
                        <h2 class="fw-bold">TryHackMe</h2>
                        <p class="text-gray">לימוד מודרך עם מכונות וירטואליות אמיתיות.</p>
                    </div>
                    <div class="alert alert-dark border-secondary">
                        <small class="text-white-force"><strong>מה עושים שם?</strong> פורצים למכונות לפי מדריך.</small>
                    </div>
                    <h5 class="mt-4 mb-2 text-white-force">איך מתחילים? (NetworkChuck):</h5>
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/fNZdXq2jXWU" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <a href="https://tryhackme.com/" target="_blank" class="btn-action btn-practice w-100 text-center mt-4">
                        הירשם ל-TryHackMe <i class="fas fa-arrow-left ms-2"></i>
                    </a>
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
    {
        "id": 1, 
        "title": "Networking Basics", 
        "duration": "25 שעות", 
        "color": "#38bdf8", 
        "icon": "fa-wifi",
        "desc": "הצעד הראשון. לומדים את מושגי היסוד: כתובות IP, איך מידע זז ברשת, ומה ההבדל בין רשת ביתית לאינטרנט העולמי.",
        "syllabus": ["כתובות IP ו-MAC", "רכיבי רשת: נתב ומתג", "סוגי רשתות: LAN/WAN"]
    },
    {
        "id": 2, 
        "title": "Packet Tracer", 
        "duration": "10 שעות", 
        "color": "#818cf8", 
        "icon": "fa-laptop-code",
        "desc": "קורס קריטי. כאן לומדים להשתמש בסימולטור של סיסקו. במקום לקנות ציוד יקר, בונים מעבדות וירטואליות.",
        "syllabus": ["התקנת התוכנה", "בניית רשת ראשונה", "שליחת חבילות מידע (Ping)"]
    },
    {
        "id": 3, 
        "title": "Networking Essentials", 
        "duration": "70 שעות", 
        "color": "#c084fc", 
        "icon": "fa-network-wired",
        "desc": "קורס הליבה. צוללים למודל ה-OSI ומבינים לעומק את הפרוטוקולים שמניעים את האינטרנט. זה הבסיס לכל תקיפת סייבר.",
        "syllabus": ["מודל 7 השכבות (OSI)", "פרוטוקולי TCP/UDP", "אבטחת רשת בסיסית"]
    },
    {
        "id": 4, 
        "title": "Intro to Cybersecurity", 
        "duration": "15 שעות", 
        "color": "#f472b6", 
        "icon": "fa-shield-alt",
        "desc": "המעבר לאבטחה. מבינים מי הם התוקפים, מה המוטיבציה שלהם, ואילו סוגי נוזקות קיימים בעולם.",
        "syllabus": ["הנדסה חברתית", "סוגי Malware", "עקרונות ההגנה (CIA)"]
    },
    {
        "id": 5, 
        "title": "Linux Unhatched", 
        "duration": "8 שעות", 
        "color": "#fbbf24", 
        "icon": "fa-terminal",
        "desc": "מערכת ההפעלה של ההאקרים. קורס קצר שמלמד להשתמש בשורת הפקודה (Terminal) בלי לפחד.",
        "syllabus": ["ניווט בתיקיות", "ניהול קבצים", "הרשאות משתמשים"]
    }
]

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, mode='courses', courses=courses_data, cisco_url="https://www.netacad.com/catalogs/learn")

@app.route('/practice')
def practice():
    return render_template_string(HTML_TEMPLATE, mode='practice')

if __name__ == '__main__':
    # הקוד הזה חיוני ל-Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
