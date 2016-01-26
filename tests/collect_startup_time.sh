FILES="
conditionals.cpp
copy.cpp
corrections.cpp
fannkuch.cpp
fasta.cpp
ifs.cpp
memops.cpp
primes.cpp
skinning.cpp
box2d.cpp
bullet.cpp
zlib.c
"

SM_ENGINE=$(grep SPIDERMONKEY_ENGINE ~/.emscripten|tail -n1|grep -Eo "/[^\']+")
V8_ENGINE=$(grep V8_ENGINE ~/.emscripten|tail -n1|grep -Eo "/[^\']+")

parse_result() {
    grep 'called after' | cut -c 21- | cut -d' ' -f1
}

sm() {
    ${SM_ENGINE} $* 4 2>&1 | parse_result
}

v8() {
    ${V8_ENGINE} $* -- 4 2>&1 | parse_result
}

for f in ${FILES}; do
    echo -n "$f sm+asm ";
    sm /tmp/emscripten_temp/sm_${f}.js;

    echo -n "$f sm+noasm ";
    sm --no-asmjs /tmp/emscripten_temp/sm-noasm_${f}.js;

    echo -n "$f sm+cheerp ";
    sm /tmp/emscripten_temp/sm-cheerp_${f}.js;

    echo -n "$f v8 ";
    v8 /tmp/emscripten_temp/v8_${f}.js;

    echo -n "$f v8+cheerp ";
    v8 /tmp/emscripten_temp/v8-cheerp_${f}.js;
done;
