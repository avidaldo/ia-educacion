npm run build && npm run serve


# NPM Commands Reference


A beginner-friendly guide to npm commands used in this Docusaurus project.

## 📚 NPM Basics

**What is npm?**  
npm (Node Package Manager) is a tool that manages JavaScript libraries (called "packages" or "dependencies") for your project.

**What is `package.json`?**  
This file lists all the dependencies your project needs and defines the scripts you can run.

---

## 🚀 Development Workflow

### Initial Setup

```bash
npm ci
```

**What it does:** Installs all dependencies listed in `package-lock.json`  
**When to use:** First time setting up the project, or after pulling new changes  
**Why `ci` instead of `install`?** `npm ci` is faster and ensures you get the exact same versions as everyone else

---

### Local Development (Dev Mode)

```bash
npm run dev
# or equivalently:
npm start
# or the shorthand:
npm run start
```

**What it does:**
- Starts a local development server
- Opens your browser to `http://localhost:3000/ia-educacion/`
- Watches for file changes and **auto-reloads** the page (hot reload)
- Shows errors and warnings in the terminal

**When to use:** When you're actively writing/editing content  
**To stop:** Press `Ctrl+C` in the terminal

**💡 Pro tip:** This is the command you'll use 90% of the time when working on the site!

**ℹ️ Note:** `npm run dev` and `npm start` are aliases - they do exactly the same thing. Use whichever you prefer!

---

### Production Build

```bash
npm run build
```

**What it does:**
- Creates an optimized, production-ready version of your site
- Outputs static files to the `build/` directory
- Minifies JavaScript and CSS
- Checks for broken links and errors

**When to use:**
- Before deploying
- To test the production version locally
- To verify everything builds without errors

**⏱️ Note:** This takes longer than `npm start` because it optimizes everything

---

### Preview Production Build

```bash
npm run serve
```

**What it does:**
- Serves the production build (from `build/` directory) locally
- Shows you exactly what the deployed site will look like

**When to use:** After `npm run build` to test the production version

**⚠️ Important:** You must run `npm run build` first! This command doesn't build, it only serves.

---

### Clear Cache

```bash
npm run clear
```

**What it does:** Clears Docusaurus cache and generated files

**When to use:**
- When you see weird behavior that doesn't match your code
- After changing configuration files
- When the site isn't updating despite your changes

**🔧 Troubleshooting:** If something seems broken, try: `npm run clear && npm start`

---

### Type Checking

```bash
npm run typecheck
```

**What it does:** Runs TypeScript type checking on configuration files

**When to use:**
- After modifying `docusaurus.config.ts` or `sidebars.ts`
- Before committing TypeScript changes

---

### Deploy to GitHub Pages

```bash
npm run deploy
```

**What it does:**
- Builds the production site
- Deploys it to the `gh-pages` branch
- Updates the live site at https://avidaldo.github.io/ia-educacion/

**When to use:** Manual deployment (usually handled by GitHub Actions)

**⚠️ Note:** You need GitHub write permissions for this to work

---

## 📋 Quick Reference Table

| Command | Speed | Use Case |
|---------|-------|----------|
| `npm ci` | Medium | First setup, after pulling changes |
| `npm start` | Fast | Daily development work |
| `npm run build` | Slow | Before deployment, testing |
| `npm run serve` | Fast | Preview production build |
| `npm run clear` | Fast | Fix caching issues |
| `npm run typecheck` | Fast | Validate TypeScript |
| `npm run deploy` | Slow | Manual deployment |

---

## 🔄 Common Workflows

### Starting Work
```bash
git pull                 # Get latest changes
npm ci                   # Update dependencies (if needed)
npm start                # Start dev server
```

### Before Committing
```bash
npm run build            # Ensure production build works
npm run typecheck        # Check TypeScript (if you changed config)
git add .
git commit -m "..."
git push
```

### Fixing Weird Issues
```bash
npm run clear            # Clear cache
rm -rf node_modules      # Delete dependencies
npm ci                   # Reinstall dependencies
npm start                # Try again
```

---

## 🆘 Troubleshooting

### "Error: Cannot find module..."
**Solution:** Run `npm ci` to install dependencies

### "Port 3000 is already in use"
**Solution:** Stop the other process or use a different port:
```bash
npm start -- --port 3001
```

### Changes not showing up
**Solution:**
```bash
npm run clear
npm start
```

### Build fails on GitHub Actions
**Solution:** Test the build locally first:
```bash
npm run build
```

---

## 💡 Tips for Beginners

1. **Always run `npm ci` after pulling changes** - Dependencies might have changed
2. **Use `npm start` for development** - It's fast and auto-reloads
3. **Test the build before pushing** - Run `npm run build` to catch errors early
4. **Clear cache when confused** - `npm run clear` fixes many mysterious issues
5. **Read error messages** - npm usually tells you exactly what's wrong

---

## 📖 Docusaurus-Specific Commands

These commands are defined in `package.json` and call Docusaurus internally:

- `npm start` → `docusaurus start`
- `npm run build` → `docusaurus build`
- `npm run serve` → `docusaurus serve`
- `npm run clear` → `docusaurus clear`

You can also run Docusaurus directly:
```bash
npx docusaurus --help
```

---

## 📚 Learn More

- [npm Documentation](https://docs.npmjs.com/)
- [Docusaurus CLI](https://docusaurus.io/docs/cli)
- [package.json Guide](https://docs.npmjs.com/cli/v8/configuring-npm/package-json)
