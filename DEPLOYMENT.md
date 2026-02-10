# 🚀 Deployment Guide for Streamlit Cloud

This guide will help you deploy the CV Screening Dashboard to Streamlit Cloud.

## 📋 Prerequisites

1. A GitHub account
2. Your code pushed to a GitHub repository
3. A Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io))

## 📁 Required Files Structure

Your repository should have this structure:

```
HR-automation/
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── junior fullstack developer/  # CV files folder
│   ├── Candidate1.pdf
│   ├── Candidate2.pdf
│   └── ...
├── dashboard.py             # Main dashboard app
├── results.csv              # Screening results
├── requirements.txt         # Python dependencies
├── packages.txt             # System dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Documentation
```

## 🔧 Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure these files are **NOT** in `.gitignore`:
- `junior fullstack developer/` (CV folder)
- `results.csv`
- `dashboard.py`
- `requirements.txt`
- `.streamlit/config.toml`

### 2. Push to GitHub

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Streamlit Cloud deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Fill in the form:
   - **Repository**: Select your repository
   - **Branch**: `main` (or your default branch)
   - **Main file path**: `dashboard.py`
5. Click "Deploy"

### 4. Wait for Deployment

- Streamlit Cloud will install dependencies from `requirements.txt` and `packages.txt`
- This usually takes 2-5 minutes
- You'll see build logs in real-time

## ✅ Verification

Once deployed, your dashboard should:
- ✅ Display all candidates from `results.csv`
- ✅ Show CV previews from `junior fullstack developer/` folder
- ✅ All filters and visualizations work
- ✅ Split-screen view functions properly

## 🔒 Security Notes

**Important**: This deployment includes CV files in the repository. Consider:

1. **Private Repository**: Make your GitHub repo private if CVs contain sensitive data
2. **Streamlit Cloud Privacy**: 
   - Free tier apps are public by default
   - Upgrade to Streamlit Cloud Teams for password protection
3. **Alternative**: Use Streamlit secrets for file storage URLs (S3, Google Drive, etc.)

## 🐛 Troubleshooting

### Issue: PDF files not displaying

**Solution**: Check that:
- CV files are committed to Git
- File names match exactly with `results.csv` `output` column
- Path in sidebar is correct: `./junior fullstack developer`

### Issue: "results.csv not found"

**Solution**: 
- Ensure `results.csv` is in the root directory
- Check it's not in `.gitignore`
- Verify it's committed to Git

### Issue: Module not found errors

**Solution**:
- Check all dependencies are in `requirements.txt`
- Use specific versions (e.g., `streamlit==1.28.0`)

### Issue: PDF rendering fails

**Solution**:
- System packages in `packages.txt` should be installed
- Try clearing cache: Settings → Clear cache → Reboot app

## 🔄 Updating Your Deployment

To update your deployed app:

```bash
# Make changes locally
git add .
git commit -m "Update dashboard"
git push

# Streamlit Cloud auto-deploys on push
```

## 📊 Monitoring

- View app logs in Streamlit Cloud dashboard
- Monitor app usage and performance
- Set up email alerts for errors

## 🎯 App URL

After deployment, your app will be available at:
```
https://YOUR_USERNAME-YOUR_REPO-BRANCH-dashboard-HASH.streamlit.app
```

You can customize this URL in Streamlit Cloud settings.

## 💡 Tips

1. **Custom Domain**: Upgrade to Streamlit Cloud Teams for custom domains
2. **Authentication**: Use Streamlit's built-in auth or implement your own
3. **Performance**: Use `@st.cache_data` for expensive operations (already implemented)
4. **Secrets**: Store API keys in Streamlit Cloud secrets (Settings → Secrets)

## 📞 Support

- Streamlit Docs: [docs.streamlit.io](https://docs.streamlit.io)
- Community Forum: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: Report bugs in your repository

---

**Happy Deploying! 🎉**
