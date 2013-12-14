let gypBuildCommand="gyp app.gyp --depth=. -f xcode -DOS=ios"
let breakdownCommand="rm -rf app.xcodeproj && rm -rf ~/Library/Developer/Xcode/DerivedData/"

let target="all"

let buildCommand=gypBuildCommand . "&&" . "xcodebuild --depth=. -target " . target . " -sdk iphoneos build"

map <Leader>r :call CleanShell(breakdownCommand)<CR>
map <Leader>rr :call CleanShell(gypBuildCommand)<CR>
map <Leader>rb :call CleanShell(buildCommand)<CR>

