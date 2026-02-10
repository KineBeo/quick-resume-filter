# ⚡ Quick Deploy to Streamlit Cloud

## 🚀 3 Steps to Deploy

### Step 1: Commit Files to Git

```bash
# Check what will be committed
git status

# Add all necessary files
git add .

# Commit with message
git commit -m "Add CV screening dashboard with PDF preview"

# Push to GitHub
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Visit: https://share.streamlit.io
2. Click "New app"
3. Select your GitHub repository
4. Set main file: `dashboard.py`
5. Click "Deploy"

### Step 3: Done! 🎉

Your app will be live in 2-5 minutes at:
```
https://[your-username]-hr-automation-main-dashboard-[hash].streamlit.app
```

## ✅ Checklist Before Deploy

Make sure these files exist:
- ✅ `dashboard.py` (main app)
- ✅ `results.csv` (screening results)
- ✅ `requirements.txt` (Python packages)
- ✅ `packages.txt` (system packages)
- ✅ `.streamlit/config.toml` (Streamlit config)
- ✅ `junior fullstack developer/` folder with PDF files

## 🔍 Verify Files Are Not Ignored

Check `.gitignore` - these should NOT be ignored:
```bash
# These must be committed:
junior fullstack developer/
results.csv
dashboard.py
```

## 🐛 Quick Troubleshooting

**Problem**: CVs not showing
- Check: `git status` - are PDFs tracked?
- Fix: Remove from `.gitignore`, then `git add` them

**Problem**: results.csv not found
- Check: Is it in root directory?
- Fix: `git add results.csv && git commit -m "Add results"`

**Problem**: Module errors
- Check: All packages in `requirements.txt`?
- Fix: Add missing packages, push again

## 📱 Share Your Dashboard

After deployment, share the URL with your team!

For detailed instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)
