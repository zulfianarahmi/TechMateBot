import telebot

TOKEN = "............."
bot = telebot.TeleBot(TOKEN)

qa_data = {
    "Data":
    [("Apa itu Data Analytics?",
      "Data Analytics adalah proses mengumpulkan, membersihkan, mengolah, dan menganalisis data untuk mendapatkan wawasan (insight) yang berguna dalam pengambilan keputusan. Ini bisa melibatkan teknik statistik, pemrograman, dan alat visualisasi data.\n\n"
      "Contoh: Perusahaan e-commerce seperti Shopee atau Tokopedia menggunakan data analytics untuk menganalisis pola belanja pelanggan agar bisa memberikan rekomendasi produk yang tepat."
      ),
     ("Apa tujuan Data Analytics?",
      "Tujuan utama *data analytics* adalah membantu organisasi atau bisnis dalam:\n\n"
      "- Mengambil keputusan yang lebih baik  (berbasis data, bukan tebakan)\n"
      "- Mengoptimalkan proses bisnis  (misalnya mengurangi biaya produksi)\n"
      "- Menganalisis tren & pola  (misalnya tren penjualan per bulan)\n"
      "- Memprediksi masa depan  (misalnya prediksi permintaan produk)\n"
      "- Meningkatkan pengalaman pelanggan  (misalnya personalisasi rekomendasi produk)\n\n"
      "Contoh: Netflix menggunakan *data analytics* untuk merekomendasikan film berdasarkan kebiasaan menonton pengguna."
      ),
     ("Apa itu ETL dalam Data Analytics?",
      "ETL (Extract, Transform, Load) adalah proses dalam *data analytics* yang melibatkan pengambilan data dari berbagai sumber, membersihkan & mengubahnya ke format yang sesuai, lalu menyimpannya di tempat penyimpanan seperti *data warehouse*.\n\n"
      "- Extract → Ambil data dari berbagai sumber (database, API, file Excel, dsb).\n"
      "- Transform → Bersihkan dan ubah format data (hapus duplikat, isi data yang kosong, dsb).\n"
      "- Load → Simpan data ke data warehouse untuk dianalisis lebih lanjut.\n\n"
      "Contoh: Perusahaan retail seperti Indomaret menggunakan ETL untuk menggabungkan data transaksi dari ribuan toko ke satu database pusat."
      ),
     ("Apa itu SQL dalam Data Analytics?",
      "SQL (Structured Query Language) adalah bahasa yang digunakan untuk mengakses dan mengelola data dalam database. Dalam *data analytics*, SQL digunakan untuk:\n\n"
      "- Mengambil data dari database\n"
      "- Memfilter & mengolah data\n"
      "- Menggabungkan data dari berbagai tabel"),
     ("Apa itu Dashboard dalam Data Analytics?",
      "Dashboard adalah tampilan visual yang menyajikan data dalam bentuk grafik, tabel, dan metrik untuk mempermudah analisis. Biasanya dibuat menggunakan alat seperti  Power BI, Tableau, atau Google Data Studio .\n\n"
      "Contoh: Perusahaan e-commerce membuat dashboard yang menampilkan jumlah order, pendapatan harian, produk terlaris, dsb, agar manajemen bisa mengambil keputusan dengan cepat."
      ),
     ("Apa itu Data Science?",
      "Data Science adalah bidang ilmu yang menggabungkan  statistik, pemrograman, dan pemahaman bisnis  untuk menganalisis data, menemukan pola, serta membuat prediksi atau keputusan berbasis data.\n\n"
      "Komponen utama Data Science: \n\n"
      "Data Collection → Mengumpulkan data dari berbagai sumber.\n"
      "Data Cleaning → Membersihkan data dari kesalahan atau nilai yang tidak relevan.\n"
      "Exploratory Data Analysis (EDA) → Menganalisis data untuk menemukan pola dan wawasan.\n"
      "Machine Learning & AI → Membangun model prediktif untuk membuat keputusan otomatis.\n"
      "Data Visualization → Menyajikan data dalam bentuk grafik atau dashboard agar mudah dipahami."
      ),
     ("Apa itu Machine Learning dalam Data Science?",
      "Machine Learning (ML) adalah cabang dari Data Science yang memungkinkan komputer belajar dari data tanpa harus diprogram secara eksplisit.\n\n"
      "Tiga jenis utama Machine Learning: \n\n"
      "1. Supervised Learning → Model belajar dari data berlabel (contoh: klasifikasi email spam).\n"
      "2. Unsupervised Learning → Model mencari pola dalam data tanpa label (contoh: segmentasi pelanggan).\n"
      "3. Reinforcement Learning → Model belajar berdasarkan sistem reward & punishment (contoh: AI dalam game seperti AlphaGo).\n\n"
      "Alat yang sering digunakan:\n\n"
      "- Scikit-learn (untuk ML dasar)\n"
      "- TensorFlow & PyTorch (untuk Deep Learning)\n"
      "- Keras (untuk Neural Networks)\n\n"
      "Contoh penggunaan Machine Learning dalam Data Science:\n\n"
      "- Google Translate menggunakan ML untuk menerjemahkan bahasa.\n"
      "- Spotify merekomendasikan lagu berdasarkan ML.\n"
      "- Perusahaan asuransi memprediksi risiko klaim menggunakan ML"),
     ("Apa itu Python dan R dalam Data Science?",
      " Python dan R  adalah dua bahasa pemrograman yang paling sering digunakan dalam  Data Science .\n\n"
      " Python dalam Data Science: \n\n"
      "- Python adalah bahasa  serbaguna  yang sering digunakan dalam  Machine Learning, AI, dan pemrosesan data .\n"
      "- Punya banyak  library powerful  seperti  NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow  untuk analisis data dan pembuatan model AI.\n"
      "- Lebih mudah dipelajari untuk pemula karena syntax-nya  mirip bahasa manusia .\n"
      "- Cocok untuk  Big Data ,  analisis skala besar , dan  deployment ke aplikasi web atau API .\n\n"
      " R dalam Data Science: \n\n"
      "- R dibuat  khusus  untuk statistik dan analisis data.\n"
      "- Punya  visualisasi data yang sangat keren  dengan  ggplot2, lattice, dan plotly .\n"
      "- Sangat kuat dalam  analisis statistik, probabilitas, dan eksplorasi data .\n"
      "- Biasanya digunakan oleh  peneliti, akademisi, dan data analyst  yang lebih fokus ke statistik.\n\n"
      " Kesimpulan: \n\n"
      "-  Gunakan Python  jika ingin bekerja di bidang  AI, Machine Learning, dan Big Data .\n"
      "-  Gunakan R  jika lebih fokus pada  statistik, riset, dan visualisasi data .\n"
      "-  Kombinasi keduanya juga bagus ! Banyak perusahaan menggunakan  R untuk analisis awal  dan  Python untuk membangun model AI ."
      ),
     ("Apa itu Model Training dalam Data Science?",
      " Model Training  dalam Data Science adalah  proses melatih model Machine Learning  agar bisa  mempelajari pola dari data  dan membuat prediksi yang akurat.\n\n"
      " Cara Kerja Model Training: \n\n"
      "1.  Menyiapkan Data  → Data dibersihkan dan dibagi menjadi  data latih (training data)  dan  data uji (testing data) .\n"
      "2.  Memilih Model  → Misalnya  Decision Tree, Random Forest, Neural Network , dll.\n"
      "3.  Melatih Model  → Model belajar dari  training data  dengan menyesuaikan parameter agar bisa mengenali pola.\n"
      "4.  Evaluasi Model  → Model diuji dengan  testing data  untuk melihat akurasinya.\n"
      "5.  Fine-tuning  → Jika hasil kurang bagus, model bisa  diperbaiki  dengan mengubah parameter atau menambah data.\n"
      "6.  Deploy Model  → Jika model sudah cukup akurat, bisa digunakan untuk  prediksi di dunia nyata .\n\n"
      " Contoh Sederhana: \n\n"
      "Kita ingin membuat model untuk  memprediksi harga rumah .\n\n"
      "-  Training:  Model diberikan data  harga rumah sebelumnya , lengkap dengan ukuran, lokasi, dll.\n"
      "-  Testing:  Model diuji dengan data baru yang belum pernah dilihat sebelumnya.\n"
      "-  Prediksi:  Model bisa memperkirakan  harga rumah baru  berdasarkan pola yang telah dipelajari.\n\n"
      " Kesimpulan:  Model Training adalah  proses utama dalam Machine Learning  di mana kita  melatih algoritma  agar bisa  mengenali pola dan membuat prediksi  dengan akurat."
      ),
     ("Apa itu AI dalam Data Science?",
      " Artificial Intelligence (AI)  dalam  Data Science  adalah penggunaan algoritma dan teknik komputasi yang memungkinkan mesin untuk belajar dari data, mengenali pola, dan membuat keputusan tanpa campur tangan manusia secara langsung. AI membantu dalam  otomatisasi, prediksi, dan pengambilan keputusan  berdasarkan data.\n\n"
      " Hubungan AI dengan Data Science: \n\n"
      "-  Data Science  → Mengolah dan menganalisis data untuk mendapatkan wawasan.\n"
      "-  Machine Learning (ML) & AI  → Menggunakan algoritma cerdas untuk belajar dari data dan membuat prediksi atau keputusan.\n\n"
      " Contoh AI dalam Data Science: \n\n"
      "-  Pengenalan Wajah  → AI mengenali wajah dalam foto untuk autentikasi (misalnya, Face ID di iPhone).\n"
      "-  Chatbot & Asisten Virtual  → AI di chatbot seperti ChatGPT atau Siri membantu menjawab pertanyaan pelanggan.\n"
      "-  Deteksi Penipuan di Bank  → AI menganalisis pola transaksi untuk mendeteksi aktivitas mencurigakan.\n"
      "-  Analisis Sentimen Media Sosial  → AI membaca komentar pelanggan untuk memahami kepuasan mereka."
      ),
     ("Apa itu Big Data dalam Data Science?",
      " Big Data dalam Data Science  adalah kumpulan data dalam jumlah besar, cepat bertambah, dan beragam yang digunakan untuk analisis dan pengambilan keputusan berbasis data.\n\n"
      " Big Data vs. Data Science: \n\n"
      "-  Big Data  → Berfokus pada penyimpanan dan pengelolaan data dalam jumlah besar.\n"
      "-  Data Science  → Berfokus pada analisis dan pemanfaatan data untuk mendapatkan wawasan.\n\n"
      " Contoh Big Data dalam Data Science: \n\n"
      "-  E-commerce (Tokopedia, Shopee, Amazon)  → Menganalisis data pembelian untuk rekomendasi produk.\n"
      "-  Kesehatan (Medical AI)  → Menganalisis jutaan rekam medis untuk prediksi penyakit.\n"
      "-  Transportasi (Google Maps, Grab, Gojek)  → Menganalisis lalu lintas untuk rute tercepat.\n"
      "-  Media Sosial (Instagram, Twitter, TikTok)  → Menggunakan data besar untuk menampilkan konten yang relevan bagi pengguna."
      ),
     ("Apa itu Data Engineering?",
      "Data Engineering adalah bidang dalam ilmu data yang berfokus pada pengumpulan, penyimpanan, pemrosesan, dan pengelolaan data agar dapat digunakan untuk analisis dan pengambilan keputusan. Data engineering memungkinkan data mengalir dari berbagai sumber ke dalam sistem yang siap digunakan oleh Data Analyst dan Data Scientist."
      ),
     ("Apa tugas utama Data Engineer?",
      "Tugas utama  Data Engineer  meliputi:\n\n"
      "1.  ETL (Extract, Transform, Load) \n"
      "    -  Extract  → Mengambil data dari berbagai sumber seperti database, API, atau file flat.\n"
      "    -  Transform  → Membersihkan dan mengubah data menjadi format yang seragam.\n"
      "    -  Load  → Menyimpan data ke dalam  data warehouse  agar siap untuk dianalisis.\n"
      "2.  Membangun dan Mengelola Data Pipeline \n"
      "    - Memastikan data mengalir dengan lancar dari sumber ke tujuan.\n"
      "    - Melakukan pembersihan dan validasi data dalam perjalanan.\n"
      "3.  Mengelola Data Warehouse \n"
      "    - Membangun struktur database agar penyimpanan data efisien dan mudah diakses.\n"
      "    - Menggunakan teknologi seperti  SQL Server, PostgreSQL, Snowflake, Redshift .\n"
      "4.  Orkestrasi dan Monitoring Data Pipeline \n"
      "    - Menjadwalkan dan mengawasi proses otomatisasi data dengan  Apache Airflow, Dagster, Prefect .\n"
      "    - Memastikan sistem berjalan stabil dan menangani error jika terjadi kegagalan.\n"
      "5.  Mengelola Data di Cloud \n"
      "    - Memanfaatkan  AWS, Azure, atau Google Cloud  untuk penyimpanan dan pemrosesan data dalam skala besar."
      ),
     ("Apa itu Data Pipeline?",
      " Data Pipeline  adalah serangkaian proses otomatis yang mengambil, memproses, dan mentransfer data dari satu sistem ke sistem lain.\n\n"
      " Contoh Sederhana: \n\n"
      "Sebuah e-commerce memiliki transaksi pelanggan dalam berbagai database di beberapa negara.  Data Pipeline  akan:\n\n"
      "- Mengambil data dari semua database transaksi.\n"
      "- Mengonversi mata uang ke USD.\n"
      "- Membersihkan data (misalnya mengisi nilai yang hilang).\n"
      "- Menyimpan data yang sudah rapi ke  data warehouse .\n\n"
      "Dengan  Data Pipeline , perusahaan dapat menganalisis data secara real-time tanpa harus melakukan pekerjaan manual."
      ),
     ("Apa itu Data Warehouse dan Data Lake?", "   Data Warehouse \n\n"
      " Data Warehouse  adalah sistem penyimpanan data yang telah  dikelola, difilter, dan disusun dengan skema tertentu  agar siap untuk analisis bisnis. Data di dalamnya sudah  diproses dan dioptimalkan  untuk query dan pelaporan.\n\n"
      " Ciri-ciri Data Warehouse: \n\n"
      "- Data sudah  terstruktur  dan siap digunakan.\n"
      "- Digunakan untuk  Business Intelligence (BI)  dan analisis historis.\n"
      "- Lebih cepat dalam pencarian karena sudah diorganisir dengan baik.\n"
      "- Contoh sistem:  Amazon Redshift, Google BigQuery, Snowflake .\n\n"
      " Contoh: \n\n"
      "Perusahaan ingin menganalisis  tren penjualan  selama 5 tahun terakhir. Semua data penjualan telah disimpan dalam  Data Warehouse , sehingga mudah untuk ditelusuri dan dibandingkan."
      ),
     ("Apa itu Apache Spark dan Hadoop?",
      "Apache Spark adalah kerangka kerja pemrosesan data terdistribusi yang dirancang untuk memproses data dengan cepat dalam skala besar. Spark lebih cepat dibanding Hadoop karena menggunakan in-memory computing, yang berarti data diproses langsung di RAM tanpa harus membaca/menulis ke disk secara berulang."
      ),
     ("Apa roadmap untuk menjadi Data Analyst?", "   Data Analyst \n\n"
      "1.  Excel & SQL  → Jago pivot table, VLOOKUP, query database.\n"
      "2.  BI Tools  → Tableau, Power BI buat dashboard.\n"
      "3.  Statistik Dasar  → Mean, median, standar deviasi, A/B Testing.\n"
      "4.  Python (Opsional, Tapi Keren)  → Pandas, Seaborn buat analisis data.\n"
      "5.  Portofolio & Apply  → Bikin proyek di Kaggle, post di GitHub/LinkedIn"
      ),
     ("Apa roadmap untuk menjadi Data Scientist?", " Python & SQL \n\n"
      "→ Wajib buat ngolah data.\n\n"
      " Matematika & Statistik \n\n"
      "→ Probabilitas, regresi, distribusi data.\n\n"
      " Machine Learning \n\n"
      "→ Scikit-learn, TensorFlow, PyTorch.\n\n"
      " EDA & Feature Engineering \n\n"
      "→ Bersihin & siapin data buat model.\n\n"
      " Portofolio & Research \n\n"
      "→ Bangun proyek ML & ikut kompetisi Kaggle."),
     ("Apa roadmap untuk menjadi Data Engineer?", " SQL & Database \n\n"
      "→ Wajib ngerti\n\n"
      " SQL, NoSQL, Data Warehousing \n\n"
      " Coding (Python, Java, Scala) \n\n"
      "→ Buat ETL & data pipeline.\n\n"
      " Big Data Tools \n\n"
      "→ Hadoop, Spark, Kafka, Airflow.\n\n"
      " Cloud & DevOps \n\n"
      "→ AWS, GCP, Docker, Kubernetes.\n\n"
      " Portofolio & Apply \n\n"
      "→ Bangun pipeline dummy, deploy di cloud.")],
    "Cloud":
    [("Apa itu Cloud Computing?",
      "Cloud Computing adalah konsep di mana data dan aplikasi disimpan serta dijalankan di server jarak jauh (cloud) melalui internet, bukan di perangkat lokal atau server fisik yang dimiliki sendiri. Cloud Computing memungkinkan akses ke layanan IT tanpa harus memiliki dan mengelola infrastruktur sendiri."
      ),
     ("Apa manfaat Cloud Computing?", " Mengurangi Biaya \n\n"
      "– Tidak perlu membeli dan merawat server sendiri, cukup membayar layanan cloud sesuai kebutuhan.\n\n"
      " Fleksibilitas & Skalabilitas \n\n"
      "– Bisa menambah atau mengurangi sumber daya sesuai permintaan (*pay-as-you-go*).\n\n"
      " Keamanan & Disaster Recovery \n\n"
      "– Penyedia cloud menyediakan backup otomatis dan perlindungan dari kegagalan server.\n\n"
      " Akses dari Mana Saja \n\n"
      "– Selama terhubung ke internet, data dan aplikasi bisa diakses dari mana saja."
      ),
     ("Apa itu Virtual Machine (VM) dalam Cloud?",
      "Virtual Machine (VM) dalam Cloud adalah mesin virtual yang berjalan di server cloud, memungkinkan pengguna untuk menjalankan sistem operasi dan aplikasi seperti di komputer fisik. VM di cloud bisa diatur, dijalankan, dan dihentikan sesuai kebutuhan tanpa harus memiliki perangkat keras fisik."
      ),
     ("Apa itu Container dalam Cloud Computing?",
      "Container dalam Cloud Computing adalah teknologi yang memungkinkan aplikasi dan semua dependensinya dikemas dalam sebuah wadah (container) yang ringan dan portabel. Container memungkinkan aplikasi berjalan konsisten di berbagai lingkungan, mulai dari development, testing, hingga production."
      ),
     ("Apa itu Serverless Computing?",
      "Serverless Computing adalah model komputasi di mana penyedia cloud mengelola infrastruktur server secara otomatis. Developer hanya perlu menulis dan menjalankan kode tanpa perlu khawatir tentang pengelolaan server. Biaya yang dikenakan biasanya berdasarkan penggunaan (pay-as-you-go)."
      ),
     ("Apa itu IaaS (Infrastructure as a Service)?",
      "IaaS (Infrastructure as a Service) adalah layanan cloud yang menyediakan infrastruktur IT seperti server, storage, dan jaringan secara virtual. Pengguna memiliki kendali penuh atas sistem operasi dan aplikasi yang dijalankan, sementara penyedia cloud mengelola infrastruktur fisik."
      ),
     ("Apa itu PaaS (Platform as a Service)?",
      "PaaS (Platform as a Service) adalah layanan cloud yang menyediakan platform untuk mengembangkan, menguji, dan menjalankan aplikasi. Developer tidak perlu mengelola infrastruktur dasar seperti server dan jaringan, sehingga bisa fokus pada pengembangan aplikasi."
      ),
     ("Apa itu SaaS (Software as a Service)?",
      "SaaS (Software as a Service) adalah layanan cloud yang menyediakan aplikasi siap pakai melalui internet. Pengguna tidak perlu menginstal atau mengelola aplikasi tersebut, cukup mengaksesnya melalui browser. Contoh: Google Workspace, Microsoft 365."
      ),
     ("Apa roadmap untuk menjadi Cloud Engineer?",
      "**1. Pelajari Dasar-Dasar Cloud**\n\n"
      "- Pahami konsep dasar Cloud Computing (IaaS, PaaS, SaaS).\n"
      "- Pelajari layanan cloud dari penyedia seperti AWS, Azure, atau Google Cloud.\n\n"
      "**2. Kuasai Linux dan Jaringan**\n\n"
      "- Pelajari command line Linux dan manajemen server.\n"
      "- Pahami dasar-dasar jaringan seperti IP, subnetting, DNS, dan firewall.\n\n"
      "**3. Pelajari Layanan Cloud Populer**\n\n"
      "- AWS: EC2, S3, Lambda, RDS.\n"
      "- Azure: Virtual Machines, Blob Storage, Functions.\n"
      "- Google Cloud: Compute Engine, Cloud Storage, Cloud Functions.\n\n"
      "**4. Pelajari Infrastructure as Code (IaC)**\n\n"
      "- Kuasai tools seperti Terraform dan CloudFormation untuk mengelola infrastruktur cloud secara otomatis.\n\n"
      "**5. Pelajari Keamanan Cloud**\n\n"
      "- Pahami konsep keamanan cloud seperti IAM, enkripsi, dan compliance.\n\n"
      "**6. Bangun Portofolio**\n\n"
      "- Buat proyek-proyek kecil seperti deploy aplikasi web di cloud atau membuat pipeline CI/CD.\n\n"
      "**7. Dapatkan Sertifikasi**\n\n"
      "- Ambil sertifikasi cloud seperti AWS Certified Solutions Architect, Azure Administrator, atau Google Cloud Professional."
      )],
    "DevOps":
    [("Apa itu DevOps?",
      "DevOps adalah pendekatan yang menggabungkan Development (Dev) dan Operations (Ops) untuk meningkatkan kolaborasi, otomatisasi, dan efisiensi dalam pengembangan perangkat lunak. DevOps membantu tim bekerja lebih cepat dan lebih andal dalam membangun, menguji, dan merilis aplikasi."
      ),
     ("Apa tujuan utama dari DevOps?", " Otomatisasi & Efisiensi \n\n"
      "→ Mengurangi kerja manual dengan pipeline CI/CD.\n\n"
      " Kolaborasi Tim \n\n"
      "→ Menghilangkan sekat antara developer & tim operasi.\n\n"
      " Delivery Cepat \n\n"
      "→ Mempercepat rilis aplikasi dengan feedback berkelanjutan.\n\n"
      " Keandalan & Stabilitas \n\n"
      "→ Memastikan sistem tetap aman dan berjalan lancar.\n\n"
      " Manfaat DevOps bagi Perusahaan: \n\n"
      "- Deployment lebih cepat & sering.\n"
      "- Produktivitas meningkat.\n"
      "- Downtime lebih sedikit.\n"
      "- Keamanan lebih baik dengan praktik  Infrastructure as Code (IaC)  & otomatisasi keamanan."
      ),
     ("Apa perbedaan DevOps dan SysAdmin?",
      "SysAdmin lebih ke pengelolaan infrastruktur IT, sedangkan DevOps lebih ke otomatisasi & integrasi antara pengembangan dan operasi. "
      ),
     ("Apa itu CI/CD dalam DevOps?",
      "CI/CD (Continuous Integration & Continuous Deployment) adalah metode DevOps yang mengotomatiskan pengembangan, pengujian, dan deployment aplikasi agar lebih cepat dan stabil.\n\n"
      " CI (Continuous Integration): \n\n"
      "- Developer sering mengunggah kode ke repository (GitHub, GitLab, dsb).\n"
      "- Kode diuji secara otomatis untuk mendeteksi bug lebih awal.\n"
      "- Memastikan setiap perubahan dapat bekerja dengan baik sebelum diintegrasikan.\n\n"
      " CD (Continuous Deployment): \n\n"
      "- Setelah lolos pengujian, kode langsung diterapkan ke server produksi.\n"
      "- Tidak ada intervensi manual dalam proses deployment.\n"
      "- Aplikasi bisa mendapatkan update dalam hitungan menit, bukan hari.\n\n"
      " Tools CI/CD yang umum digunakan:  Jenkins, GitHub Actions, GitLab CI/CD, CircleCI, TeamCity\n\n"
      " Kesimpulan:  CI/CD memungkinkan perusahaan untuk lebih  cepat, efisien, dan minim bug dalam merilis software baru. "
      ),
     ("Apa itu Containerization dalam DevOps?",
      "Containerization adalah teknik dalam DevOps yang memungkinkan aplikasi dan semua dependensinya dikemas dalam container, sehingga bisa dijalankan di berbagai lingkungan dengan cara yang lebih ringan dibandingkan virtual machine (VM)."
      ),
     ("Apa roadmap untuk menjadi DevOps Engineer?", " Linux Fundamentals \n\n"
      "- Pelajari  command line ,  bash scripting , dan  manajemen server .\n\n"
      " Networking Basics \n\n"
      "- Pahami  IP, subnetting, DNS, HTTP/HTTPS, SSH , dan  firewall .\n\n"
      " Git & Version Control \n\n"
      "- Gunakan  Git  untuk tracking perubahan kode & kolaborasi.\n\n"
      " Programming (Python, Go, Bash) \n\n"
      "- Automasi tugas & manajemen konfigurasi.\n\n"
      " Cloud Computing (AWS, Azure, GCP) \n\n"
      "- Pelajari  deploy aplikasi, storage, IAM, dan networking cloud .\n\n"
      " Containerization (Docker, Podman) \n\n"
      "- Isolasi aplikasi dalam  container  untuk kemudahan deploy.\n\n"
      " CI/CD (Jenkins, GitHub Actions, GitLab CI/CD) \n\n"
      "- Automasi build, test, dan deployment kode.\n\n"
      " Orchestration (Kubernetes, Helm) \n\n"
      "- Kelola  scalability  dan  deployment  aplikasi berbasis container.\n\n"
      " Infrastructure as Code (Terraform, Ansible) \n\n"
      "- Automasi provisioning server dan konfigurasi.\n\n"
      " Monitoring & Logging (Prometheus, Grafana, ELK) \n\n"
      "- Pantau kinerja server dan aplikasi."),
     ("Apa itu Kubernetes?",
      "Kubernetes (K8s) adalah sistem orkestrasi container yang digunakan untuk mengelola, mengatur, dan mengotomatisasi deployment, scaling, serta operasi containerized applications. Kubernetes sangat berguna dalam lingkungan DevOps untuk memastikan aplikasi berjalan stabil dan dapat diskalakan dengan efisien."
      ),
     ("Apa itu Terraform?",
      "Terraform adalah tools Infrastructure as Code (IaC) yang digunakan untuk mengotomatisasi dan mengelola infrastruktur IT (server, jaringan, database, dll.) menggunakan kode."
      )]
}

user_state = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Halo! Saya TechMateBot. Pilih topik yang ingin kamu pelajari:\n\n"
        "*Data*\n*Cloud*\n*DevOps*\n\n"
        "Ketik nama topiknya untuk melihat daftar pertanyaan.",
        parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text.strip().lower() in
                     [t.lower() for t in qa_data])
def choose_topic(message):
    topic_input = message.text.strip().lower()

    matched_topic = next((t for t in qa_data if t.lower() == topic_input),
                         None)

    if matched_topic:
        user_state[message.chat.id] = {
            "topic": matched_topic
        }  # Simpan topik yang dipilih user

        questions = "\n".join(f"{i+1}. {q[0]}"
                              for i, q in enumerate(qa_data[matched_topic]))
        bot.reply_to(
            message,
            f"Kamu memilih topik *{matched_topic}*. Pilih pertanyaan yang ingin kamu tanyakan dengan mengetik angkanya:\n\n{questions}",
            parse_mode="Markdown")
    else:
        bot.reply_to(
            message,
            "Maaf, topik tidak ditemukan. Coba ketik 'Data', 'Cloud', atau 'DevOps'."
        )


@bot.message_handler(func=lambda message: message.chat.id in user_state)
def answer_question(message):
    user_id = message.chat.id
    state = user_state[user_id]  # Ambil status user
    topic = state["topic"]

    if message.text.isdigit():  # Cek apakah input adalah angka
        question_index = int(message.text) - 1  # Konversi input ke index
        if 0 <= question_index < len(qa_data[topic]):
            question, answer = qa_data[topic][question_index]
            bot.reply_to(message, f"*{question}*\n\n{answer}\n\n"
                         " Mau bertanya lagi?\n"
                         " Ketik angka lain untuk bertanya\n"
                         "Ketik /back Jika sudah selesai",
                         parse_mode="Markdown")
        else:
            bot.reply_to(
                message,
                " Nomor yang kamu pilih tidak valid. Pilih angka dari daftar ya!"
            )
    else:
        bot.reply_to(
            message, "Terima kasih telah menggunakan TechMateBot! 🤖🚀\n\n"
            "Semoga informasi ini bermanfaat. Kalau masih bingung, tenang… saya juga suka diajak ngobrol lagi! 😆\n\n"
            "Jika ada pertanyaan lebih lanjut (atau ada yang error 😅), jangan ragu untuk menghubungi pemilik saya, Zulfiana Rahmi!"
        )

print("🤖 Bot sedang berjalan...")

bot.polling(none_stop=True)
