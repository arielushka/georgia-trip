from flask import Flask, render_template_string

app = Flask(__name__)

# --- תבנית ה-HTML וה-CSS בתוך הקוד (כדי שזה יעבוד בקובץ אחד) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Roadmap - הדרך לסייבר</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-dark: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #0ea5e9;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Rubik', sans-serif;
            overflow-x: hidden;
        }

        /* כותרת ראשית */
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

        /* כרטיסי הקורסים */
        .timeline-card {
            background: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .timeline-card:hover {
            transform: translateX(-5px);
            border-color: var(--accent);
            box-shadow: 0 10px 30px rgba(14, 165, 233, 0.15);
        }

        .course-number {
            position: absolute;
            top: -10px;
            left: -10px;
            font-size: 80px;
            font-weight: 900;
            color: rgba(255,255,255,0.03);
            z-index: 0;
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
            margin-left: 15px;
        }

        /* כרטיס התרגול */
        .practice-card {
            background: linear-gradient(145deg, #1e293b, #0f172a);
            border: 1px solid #ef4444;
            border-radius: 16px;
            position: sticky;
            top: 20px;
        }

        .btn-glow {
            background: transparent;
            border: 2px solid var(--accent);
            color: var(--accent);
            font-weight: 600;
            transition: 0.3s;
        }

        .btn-glow:hover {
            background: var(--accent);
            color: white;
            box-shadow: 0 0 20px var(--accent);
        }

        .btn-practice {
            background: #ef4444;
            border: none;
            color: white;
            font-weight: 700;
        }
        
        .btn-practice:hover {
            background: #dc2626;
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.6);
        }
    </style>
</head>
<body>

    <div class="hero-section">
        <div class="container">
            <h1 class="display-4 hero-title mb-3">CYBER ROADMAP</h1>
            <p class="lead text-muted mb-4">מפת הדרכים: מרשתות בסיסיות ועד תקיפה</p>
            <a href="https://www.netacad.com/catalogs/learn" target="_blank" class="btn btn-glow px-5 rounded-pill">
                לקטלוג הקורסים של Cisco <i class="fas fa-external-link-alt me-2"></i>
            </a>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row g-5">
            <div class="col-lg-8">
                <h3 class="mb-4 text-white border-end border-4 border-info pe-3">
                    <i class="fas fa-road ms-2"></i>מסלול הלימוד
                </h3>

                {% for course in courses %}
                <div class="timeline-card">
                    <span class="course-number">{{ course.id }}</span>
                    <div class="d-flex align-items-center position-relative" style="z-index: 1;">
                        <div class="icon-box" style="color: {{ course.color }}; border: 1px solid {{ course.color }}">
                            <i class="fas {{ course.icon }}"></i>
                        </div>
                        <div class="flex-grow-1">
                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <h5 class="mb-0 fw-bold text-white">{{ course.title }}</h5>
                                <span class="badge bg-dark border border-secondary">
                                    {{ course.duration }}
                                </span>
                            </div>
                            <p class="text-muted small mb-0">{{ course.description }}</p>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>

            <div class="col-lg-4">
                <h3 class="mb-4 text-white border-end border-4 border-danger pe-3">
                    <i class="fas fa-dumbbell ms-2"></i>זמן תרגול
                </h3>
                
                <div class="card practice-card p-4 text-center">
                    <div class="mb-3 text-danger display-4">
                        <i class="fas fa-biohazard"></i>
                    </div>
                    <h4 class="fw-bold mb-2 text-white">TryHackMe Labs</h4>
                    <p class="text-muted small mb-4">אל תחכה לסוף. תרגל במקביל ללמידה.</p>
                    
                    <div class="alert alert-dark text-start border-0 bg-opacity-10 bg-white mb-4">
                        <small class="d-block text-white mb-1"><strong>מתי לתרגל?</strong></small>
                        <span class="text-muted small">מומלץ להתחיל במקביל לקורס 'Networking Essentials'.</span>
                    </div>

                    <a href="https://tryhackme.com/path/outline/presecurity" target="_blank" class="btn btn-practice w-100 py-2 rounded-3">
                        התחל לתרגל <i class="fas fa-arrow-left ms-2"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
"""

# --- הנתונים (Data) ---
courses_data = [
    {"id": 1, "title": "Networking Basics", "duration": "25 שעות", "description": "הבסיס: כתובות IP, תקשורת ומושגי יסוד.", "icon": "fa-wifi", "color": "#38bdf8"},
    {"id": 2, "title": "Packet Tracer", "duration": "10 שעות", "description": "חובה! הסימולטור לבניית רשתות וירטואליות.", "icon": "fa-laptop-code", "color": "#818cf8"},
    {"id": 3, "title": "Networking Essentials", "duration": "70 שעות", "description": "הקורס המרכזי. מודל ה-OSI, פרוטוקולים, ניתוב ואבטחה.", "icon": "fa-network-wired", "color": "#c084fc"},
    {"id": 4, "title": "Intro to Cybersecurity", "duration": "15 שעות", "description": "מבוא לאיומים, נוזקות, והגנה על מידע.", "icon": "fa-shield-alt", "color": "#f472b6"},
    {"id": 5, "title": "Linux Unhatched", "duration": "8 שעות", "description": "הכרת הטרמינל (שורת הפקודה) של לינוקס.", "icon": "fa-terminal", "color": "#fbbf24"}
]

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, courses=courses_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
