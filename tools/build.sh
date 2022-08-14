conan install -if ../conanfiles -pr:b=default --update --build=missing ../ &&
conan build   -if ../conanfiles -bf ../build ../                           &&
../build/conan_test
