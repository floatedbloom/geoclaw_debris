
export BASE_URL=/clawpack/geoclaw/geoclaw_debris
#rm -rf _build  # necessary?
jupyter book build --html --execute

echo Next:
echo '   rsync -avz _build/html/ clawpack@homer.u.washington.edu:public_html/geoclaw/geoclaw_debris/'

echo Then:
echo '  open http://depts.washington.edu/clawpack/geoclaw/geoclaw_debris/'
