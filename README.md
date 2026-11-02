# TUTIMI — Personal Web Platform & Infrastructure Showcase

The personal portfolio and technical platform engineered by **Michell Valenzuela (Tutimi)**, Senior Infrastructure Engineer & Cloud Architect.

---

## 🏗️ Cloud Infrastructure & Architecture

- **Single-EC2 Multi-Tenant Setup:** Engineered a dual-container architecture running isolated Python/Django and PHP/Laravel applications on a single AWS EC2 instance (Ubuntu AMI).
- **Traffic Routing & SSL:** Nginx serves as the primary reverse proxy handling SSL termination via Let's Encrypt / Certbot, static file delivery, and routing to container sockets.
- **Dynamic Content Engine:** Server-side experience calculation dynamically updated directly from system context without static manual updates.
- **SEO & Social Optimization:** Full Open Graph (OG) protocol implementation, structured meta tags, and optimized vector (SVG) and raster favicons.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12, Django 5.x
- **Frontend:** Alpine.js, HTML5/CSS3, SVG Vector Graphics
- **Orchestration & Infrastructure:** Docker, Docker Compose, Nginx, AWS EC2

---

## 🔒 Security Posture & Future Roadmap

- **Host-Level Hardening:** Active intrusion prevention configured via **Fail2ban** and strict AWS Security Group ingress rules limiting SSH and administrative exposure.
- **Phase 2 (Roadmap):** MariaDB / AWS RDS integration, edge WAF implementation, CDN distribution, and DDoS mitigation scheduled via Cloudflare integration.

---

## 🎯 Local Development Setup

Follow these instructions to run the Django web application locally using Docker Compose.

### 1. Shared Docker Network
Ensure the external Docker network (`la_network`) exists on your host:

```bash
docker network create la_network
```

### 2. Environment Configuration
Clone the repository and prepare your environment variables:

```bash
git clone https://github.com/michelltutimi/tutimi-platform.git
cd tutimi-platform
cp .env.example .env
```

### 3. Build and Start Container Stack
Build and launch the application container in detached mode:

```bash
docker compose up -d --build
```

Once running, the site will be accessible locally at http://localhost:8000.