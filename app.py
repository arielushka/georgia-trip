from flask import Flask, render_template_string

app = Flask(__name__)

# --- נתוני הקורסים והתרגול ---
def get_data():
    courses = [
        {
            "id": 1,
            "title": "Networking Basics",
            "duration": "25 שעות",
            "description": "הצעד הראשון. כאן לומדים את השפה של הרשת: מה זה IP, איך מידע זז, ומושגי יסוד בתקשורת.",
            "icon": "fa-wifi",
            "color": "#38bdf8"
        },
        {
            "id": 2,
            "title": "Packet Tracer",
            "duration": "10 שעות",
            "description": "חובה! זה הסימולטור של סיסקו. בלי זה אי אפשר לתרגל בניית רשתות. זה המעבדה הוירטואלית שלך.",
            "icon": "fa-laptop-code",
            "color": "#818cf8"
        },
        {
            "id": 3,
            "title": "Networking Essentials",
            "duration": "70 שעות",
            "description": "הקורס המרכזי. צלילה עמוקה למודל ה-OSI (כל 7 השכבות), פרוטוקולים, ניתוב ואבטחה ברמה גבוהה.",
            "icon": "fa-network-wired",
            "color": "#c084fc"
        },
        {
            "id": 4,
            "title": "Introduction to Cybersecurity",
            "duration": "15 שעות",
            "description": "הגשר לעולם האבטחה. הבנה של איומים, נוזקות, והגנה על המידע בארגון.",
            "icon": "fa-shield-alt",
            "color": "#f472b6"
        },
        {
            "id": 5,
            "title": "NDG Linux Unhatched",
            "duration": "8 שעות",
            "description": "הכרחי להאקרים. קורס קצר שמלמד אותך לא לפחד מהמסך השחור (הטרמינל) של לינוקס.",
            "icon": "fa-terminal",
            "color": "#fbbf24"
        }
    ]

    practice = {
        "title": "מעבדת תרגול (Hands-On)",
        "site_name": "TryHackMe - Pre Security",
        "site_url": "https://tryhackme.com/path/outline/presecurity",
        "desc": "תיאוריה זה נחמד, אבל כאן מלכלכים את הידיים.",
        "when": "מומלץ להתחיל במקביל לקורס 'Networking Essentials'. ברגע שאתה לומד מושג חדש, לך לשם לראות איך הוא נראה בזמן אמת."
    }
    
    cisco_url = "https://www.netacad.com/catalogs/learn"
    
    return courses, practice, cisco_url

# --- תבנית ה-HTML וה-CSS בתוך הקוד ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>מפת הדרכים לסייבר</title>
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
            text-shadow: 0 0 30px rgba(56, 189, 248, 0.3);
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
            transform: translateX(-10px);
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
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            background: rgba(255,255,255,0.05);
            margin-left: 20px;
        }

        /* כרטיס התרגול */
        .practice-card {
            background: linear-gradient(145deg, #1e293b, #0f172a);
            border: 1px solid #ef4444;
            border-radius: 16px;
            position: sticky;
            top: 20px;
        }

        .practice-card:hover {
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);
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

        /* אנימציות כניסה */
        .fade-up {
            animation: fadeUp 0.8s ease-out forwards;
            opacity: 0;
            transform: translateY(20px);
        }

        @keyframes fadeUp {
            to { opacity: 1; transform: translateY(0); }
        }

    </style>
</head>
<body>

    <div class="hero-section fade-up">
        <div class="container">
            <h1 class="display-3 hero-title mb-3">CYBER ROADMAP</h1>
            <p class="lead text-muted mb-4">מפת הדרכים המלאה: מרשתות בסיסיות ועד יכולות תקיפה</p>
            <a href="{{ cisco_url }}" target="_blank" class="btn btn-glow btn-lg px-5 rounded-pill">
                <i class="fas fa-external-link-alt ms-2"></i> לאתר הקורסים של Cisco
            </a>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row g-5">
            
            <div class="col-lg-8">
                <h3 class="mb-4 border-end border-4 border-info pe-3 fade-up" style="animation-delay: 0.1s">
                    <i class="fas fa-road ms-2"></i>מסלול הלימוד המומלץ
                </h3>

                {% for course in courses %}
                <div class="timeline-card fade-up" style="animation-delay: {{ loop.index * 0.1 + 0.2 }}s">
                    <span class="course-number">{{ course.id }}</span>
                    <div class="d-flex align-items-center position-relative" style="z-index: 1;">
                        <div class="icon-box" style="color: {{ course.color }}; border: 1px solid {{ course.color }}">
                            <i class="fas {{ course.icon }}"></i>
                        </div>
                        <div class="flex-grow-1">
                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <h4 class="mb-0 fw-bold">{{ course.title }}</h4>
                                <span class="badge bg-dark border border-secondary p-2">
                                    <i class="far fa-clock ms-1"></i> {{ course.duration }}
                                </span>
                            </div>
                            <p class="text-muted mb-0">{{ course.description }}</p>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>

            <div class="col-lg-4">
                <div class="fade-up" style="animation-delay: 0.8s">
                    <h3 class="mb-4 border-end border-4 border-danger pe-3">
                        <i class="fas fa-dumbbell ms-2"></i>זמן תרגול
                    </h3>
                    
                    <div class="card practice-card p-4 text-center">
                        <div class="mb-3 text-danger display-4">
                            <i class="fas fa-biohazard"></i>
                        </div>
                        <h4 class="fw-bold mb-2">{{ practice.title }}</h4>
                        <p class="text-muted small mb-4">{{ practice.desc }}</p>
                        
                        <div class="alert alert-dark text-start border-0 bg-opacity-10 bg-white mb-4">
                            <small class="d-block text-white mb-1"><i class="fas fa-info-circle text-info ms-1"></i> <strong>מתי לתרגל?</strong></small>
                            <span class="text-muted small">{{ practice.when }}</span>
                        </div>

                        <a href="{{ practice.site_url }}" target="_blank" class="btn btn-practice w-100 py-3 rounded-3">
                            התחל לתרגל ב-{{ practice.site_name }} <i class="fas fa-arrow-left ms-2"></i>
                        </a>
                    </div>
                </div>
            </div>

        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    courses, practice, cisco_url = get_data()
    return render_template_string(HTML_TEMPLATE, courses=courses, practice=practice, cisco_url=cisco_url)

if __name__ == '__main__':
    app.run(debug=True)
