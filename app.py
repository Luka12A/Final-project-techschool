from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    popular_products = [
    {
        "image": "assets/main-image-1.png",
        "title": "IBM Front-End Developer",
        "image1": "assets/star.png",
        "review": "4.6",
        "views": "4.8K reviews",
        "certificate": "Beginner . Professional Certificate . 3 - 6 Months"
    },
    {
        "image": "assets/main-image-2.png",
        "title": "Google Data Analytics",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "5.2K reviews",
        "certificate": "Beginner . Professional Certificate . 6 Months"
    },
    {
        "image": "assets/main-image-3.png",
        "title": "Meta Back-End Developer",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.5K reviews",
        "certificate": "Intermediate . Professional Certificate . 4 - 7 Months"
    },
    {
        "image": "assets/main-image-20.png",
        "title": "Cloud Solutions Architect",
        "image1": "assets/star.png",
        "review": "4.9",
        "views": "6.4K reviews",
        "certificate": "Advanced . Professional Certificate . 8 - 10 Months"
        }
    ]

    popular_products_2 = [
         {
        "image": "assets/main-image-4.png",
        "title": "AWS Cloud Practitioner",
        "description": "Skills you'll gain: Cloud architecture, storage, and security basics.",
        "image1": "assets/star.png",
        "review": "4.9",
        "views": "3.8K reviews",
        "certificate": "Beginner . Professional Certificate . 3 - 5 Months"
    },
    {
        "image": "assets/main-image-5.png",
        "title": "Cybersecurity Analyst",
        "description": "Skills you'll gain: Network security, threat management, and forensics.",
        "image1": "assets/star.png",
        "review": "4.6",
        "views": "4.3K reviews",
        "certificate": "Intermediate . Professional Certificate . 6 Months"
    },
    {
        "image": "assets/main-image-6.png",
        "title": "Microsoft AI Fundamentals",
        "description": "Skills you'll gain: Machine learning, AI principles, and tools.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "5.0K reviews",
        "certificate": "Beginner . Professional Certificate . 2 - 4 Months"
    },
     {
        "image": "assets/main-image-19.png",
        "title": "Network Administration",
        "description": "Skills you'll gain: Network configuration, troubleshooting, and virtualization.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.1K reviews",
        "certificate": "Intermediate . Certificate of Completion . 4 Months"
    },
    ]

    popular_products_3 = [
    {
        "image": "assets/main-image-7.png",
        "title": "UX Design Fundamentals",
        "description": "Skills you'll gain: User research, wireframing, and prototyping.",
        "image1": "assets/star.png",
        "review": "4.5",
        "views": "3.6K reviews",
        "certificate": "Beginner . Professional Certificate . 4 Months"
    },
    {
        "image": "assets/main-image-8.png",
        "title": "Python Programming ",
        "description": "Skills you'll gain: Python syntax, loops, and data structures.",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "6.3K reviews",
        "certificate": "Beginner . Certificate of Completion . 3 Months"
    },
    {
        "image": "assets/main-image-9.png",
        "title": "Blockchain Essentials",
        "description": "Skills you'll gain: Blockchain, cryptocurrency, and smart contracts.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "2.8K reviews",
        "certificate": "Intermediate . Professional Certificate . 5 - 7 Months"
    },
     {
        "image": "assets/main-image-15.png",
        "title": "DevOps Engineer",
        "description": "Skills you'll gain: CI/CD, Kubernetes, and infrastructure management.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.7K reviews",
        "certificate": "Advanced . Professional Certificate . 8 Months"
    }
    ]
   
    return render_template('index.html',  popular_products=popular_products, popular_products_2=popular_products_2, popular_products_3=popular_products_3)



@app.route('/courses')
def courses():

    products = [
    {
        "image": "assets/main-image-1.png",
        "title": "IBM Front-End Developer",
        "description": "Skills you'll gain: HTML, CSS, JavaScript, and React for building user interfaces.",
        "image1": "assets/star.png",
        "review": "4.6",
        "views": "4.8K reviews",
        "certificate": "Beginner . Professional Certificate . 3 - 6 Months"
    },
    {
        "image": "assets/main-image-2.png",
        "title": "Google Data Analytics",
        "description": "Skills you'll gain: Data visualization, SQL, and spreadsheets.",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "5.2K reviews",
        "certificate": "Beginner . Professional Certificate . 6 Months"
    },
    {
        "image": "assets/main-image-3.png",
        "title": "Meta Back-End Developer",
        "description": "Skills you'll gain: APIs, databases, and server-side programming.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.5K reviews",
        "certificate": "Intermediate . Professional Certificate . 4 - 7 Months"
    },
    {
        "image": "assets/main-image-4.png",
        "title": "AWS Cloud Practitioner",
        "description": "Skills you'll gain: Cloud architecture, storage, and security basics.",
        "image1": "assets/star.png",
        "review": "4.9",
        "views": "3.8K reviews",
        "certificate": "Beginner . Professional Certificate . 3 - 5 Months"
    },
    {
        "image": "assets/main-image-5.png",
        "title": "Cybersecurity Analyst",
        "description": "Skills you'll gain: Network security, threat management, and forensics.",
        "image1": "assets/star.png",
        "review": "4.6",
        "views": "4.3K reviews",
        "certificate": "Intermediate . Professional Certificate . 6 Months"
    },
    {
        "image": "assets/main-image-6.png",
        "title": "Microsoft AI Fundamentals",
        "description": "Skills you'll gain: Machine learning, AI principles, and tools.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "5.0K reviews",
        "certificate": "Beginner . Professional Certificate . 2 - 4 Months"
    },
    {
        "image": "assets/main-image-7.png",
        "title": "UX Design Fundamentals",
        "description": "Skills you'll gain: User research, wireframing, and prototyping.",
        "image1": "assets/star.png",
        "review": "4.5",
        "views": "3.6K reviews",
        "certificate": "Beginner . Professional Certificate . 4 Months"
    },
    {
        "image": "assets/main-image-8.png",
        "title": "Python Programming ",
        "description": "Skills you'll gain: Python syntax, loops, and data structures.",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "6.3K reviews",
        "certificate": "Beginner . Certificate of Completion . 3 Months"
    },
    {
        "image": "assets/main-image-9.png",
        "title": "Blockchain Essentials",
        "description": "Skills you'll gain: Blockchain, cryptocurrency, and smart contracts.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "2.8K reviews",
        "certificate": "Intermediate . Professional Certificate . 5 - 7 Months"
    },
    {
        "image": "assets/main-image-10.png",
        "title": "Digital Marketing",
        "description": "Skills you'll gain: SEO, social media marketing, and analytics.",
        "image1": "assets/star.png",
        "review": "4.6",
        "views": "5.4K reviews",
        "certificate": "Beginner . Professional Certificate . 6 - 8 Months"
    },
    {
        "image": "assets/main-image-11.png",
        "title": "Full Stack Web Developer",
        "description": "Skills you'll gain: Front-end, back-end, and database management.",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "7.2K reviews",
        "certificate": "Intermediate . Professional Certificate . 8 - 12 Months"
    },
    {
        "image": "assets/main-image-12.png",
        "title": "Machine Learning ",
        "description": "Skills you'll gain: Algorithms, TensorFlow, and model deployment.",
        "image1": "assets/star.png",
        "review": "4.9",
        "views": "6.0K reviews",
        "certificate": "Advanced . Professional Certificate . 10 Months"
    },
    {
        "image": "assets/main-image-13.png",
        "title": "Business Analytics",
        "description": "Skills you'll gain: Predictive analytics, business intelligence, and Excel.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.2K reviews",
        "certificate": "Beginner . Certificate of Completion . 5 Months"
    },
    {
        "image": "assets/main-image-14.png",
        "title": "Game Development",
        "description": "Skills you'll gain: Unity, C#, and game physics.",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "3.5K reviews",
        "certificate": "Intermediate . Certificate of Completion . 7 Months"
    },
    {
        "image": "assets/main-image-15.png",
        "title": "DevOps Engineer",
        "description": "Skills you'll gain: CI/CD, Kubernetes, and infrastructure management.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.7K reviews",
        "certificate": "Advanced . Professional Certificate . 8 Months"
    },
    {
        "image": "assets/main-image-16.png",
        "title": "Data Science Essentials",
        "description": "Skills you'll gain: Data visualization, and Python for data science.",
        "image1": "assets/star.png",
        "review": "4.9",
        "views": "6.8K reviews",
        "certificate": "Beginner . Certificate of Completion . 5 Months"
    },
    {
        "image": "assets/main-image-17.png",
        "title": "Mobile App Development",
        "description": "Skills you'll gain: Android, iOS, and cross-platform tools.",
        "image1": "assets/star.png",
        "review": "4.6",
        "views": "5.9K reviews",
        "certificate": "Intermediate . Certificate of Completion . 6 Months"
    },
    {
        "image": "assets/main-image-18.png",
        "title": "AI Chatbot Development",
        "description": "Skills you'll gain: NLP, conversational AI, and chatbot deployment.",
        "image1": "assets/star.png",
        "review": "4.8",
        "views": "3.3K reviews",
        "certificate": "Advanced . Certificate of Completion . 5 - 8 Months"
    },
    {
        "image": "assets/main-image-19.png",
        "title": "Network Administration",
        "description": "Skills you'll gain: Network configuration, troubleshooting, and virtualization.",
        "image1": "assets/star.png",
        "review": "4.7",
        "views": "4.1K reviews",
        "certificate": "Intermediate . Certificate of Completion . 4 Months"
    },
    {
        "image": "assets/main-image-20.png",
        "title": "Cloud Solutions Architect",
        "description": "Skills you'll gain: Cloud infrastructure, migration, and cost optimization.",
        "image1": "assets/star.png",
        "review": "4.9",
        "views": "6.4K reviews",
        "certificate": "Advanced . Professional Certificate . 8 - 10 Months"
        }
    ]

    return render_template('courses.html', products=products)
   

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
 