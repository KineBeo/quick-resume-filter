# 🎯 START HERE - CV Screening Dashboard

## ✨ What's New?

Your CV Screening Dashboard now includes:
- ✅ **Split-screen view**: See candidate info + CV preview side-by-side
- ✅ **PDF Preview**: View original CVs directly in the dashboard
- ✅ **Streamlit Cloud Ready**: Optimized structure for deployment
- ✅ **19 CVs tracked**: All candidate CVs included

## 🚀 Quick Start

### Option 1: Run Locally (Test First)

```bash
# Navigate to project
cd /Users/kienbeovl/Downloads/HR-automation

# Run dashboard
streamlit run dashboard.py
```

The dashboard will open at `http://localhost:8501`

### Option 2: Deploy to Streamlit Cloud

```bash
# 1. Commit all changes
git add .
git commit -m "Add CV screening dashboard with PDF preview"
git push origin main

# 2. Go to https://share.streamlit.io
# 3. Click "New app"
# 4. Select your repo, set main file to "dashboard.py"
# 5. Click "Deploy"
```

**Done in 3 minutes!** 🎉

## 📁 Project Structure

```
HR-automation/
├── dashboard.py                       ⭐ Main app (updated)
├── results.csv                        📊 Screening results
├── junior fullstack developer/        📄 19 CV files
├── requirements.txt                   📦 Python packages
├── packages.txt                       🔧 System packages (new)
├── .streamlit/config.toml            ⚙️ Streamlit config (new)
│
├── START_HERE.md                      👈 You are here
├── QUICK_DEPLOY.md                    ⚡ 3-step deploy guide
├── DEPLOYMENT.md                      📖 Detailed deployment
└── DEPLOYMENT_CHECKLIST.md            ✅ Complete checklist
```

## 🎨 Dashboard Features

### 1. Overview Metrics
- Total CVs processed: **19**
- Candidates passed
- Average score
- Highest score

### 2. Interactive Filters
- Filter by job level
- Filter by pass status
- Score range slider

### 3. Visualizations
- Score distribution histogram
- Pass rate by level chart

### 4. Top Candidates
- View top N candidates
- See CV availability status
- Quick preview toggle

### 5. Split-Screen Candidate Details ⭐ NEW
**Left Panel:**
- Score metrics & rating
- Educational qualification
- Job history
- Skills
- Justification

**Right Panel:**
- Original CV preview (PDF viewer)
- Full-screen PDF display

## 📚 Documentation Guide

Choose based on your need:

| Document | Use When |
|----------|----------|
| **START_HERE.md** | First time setup (you are here) |
| **QUICK_DEPLOY.md** | Ready to deploy in 3 steps |
| **DEPLOYMENT.md** | Need detailed deployment guide |
| **DEPLOYMENT_CHECKLIST.md** | Want step-by-step checklist |

## 🔧 Configuration

### CV Folder Path
Default: `./junior fullstack developer`

You can change this in the dashboard sidebar if needed.

### Results File
Default: `results.csv` in root directory

## ✅ Pre-Deployment Checklist

Before deploying, verify:
- ✅ All 19 CV PDFs are in `junior fullstack developer/`
- ✅ `results.csv` exists in root directory
- ✅ `requirements.txt` has all dependencies
- ✅ `.gitignore` doesn't exclude CV folder
- ✅ All files are committed to Git

Run this to check:
```bash
git status
git ls-files | grep -E "(pdf|csv)" | wc -l
# Should show 20 (19 PDFs + 1 CSV)
```

## 🐛 Common Issues

### Issue: "results.csv not found"
**Fix:** Ensure `results.csv` is in root directory and committed to Git

### Issue: CVs not displaying
**Fix:** Check CV folder path in sidebar matches actual folder name

### Issue: PDF rendering fails
**Fix:** Ensure `packages.txt` is included (already done)

## 🎯 Next Steps

1. **Test Locally** (Recommended)
   ```bash
   streamlit run dashboard.py
   ```
   - Verify all features work
   - Check CV previews load
   - Test filters and charts

2. **Deploy to Streamlit Cloud**
   - See `QUICK_DEPLOY.md` for 3-step guide
   - Or `DEPLOYMENT.md` for detailed instructions

3. **Share with Team**
   - Copy the deployed app URL
   - Share with stakeholders

## 💡 Tips

- **Private Data**: Consider making GitHub repo private
- **Custom URL**: Available with Streamlit Cloud upgrade
- **Updates**: Just `git push` to auto-deploy changes
- **Monitoring**: View logs in Streamlit Cloud dashboard

## 🔒 Security Note

⚠️ This deployment includes CV files with personal information.

**Recommendations:**
1. Make GitHub repository private
2. Use Streamlit Cloud Teams for password protection
3. Ensure GDPR/privacy compliance

## 📞 Need Help?

- **Quick Deploy**: See `QUICK_DEPLOY.md`
- **Detailed Guide**: See `DEPLOYMENT.md`
- **Checklist**: See `DEPLOYMENT_CHECKLIST.md`
- **Streamlit Docs**: https://docs.streamlit.io
- **Community**: https://discuss.streamlit.io

---

## 🚀 Ready to Deploy?

Choose your path:

### Path A: Test First (Recommended)
```bash
streamlit run dashboard.py
```

### Path B: Deploy Now
See `QUICK_DEPLOY.md` → 3 steps → Done! 🎉

---

**Happy Screening! 📊✨**
