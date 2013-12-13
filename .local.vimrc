let buildCommand="gyp app.gyp --depth=. -f xcode -DOS=ios"
let breakdownCommand="rm -rf app.xcodeproj && rm -rf ~/Library/Developer/Xcode/DerivedData/"

map <Leader>r :call CleanShell(breakdownCommand)<CR>
map <Leader>rr :call CleanShell(buildCommand)<CR>



