from os import path
from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake
from conan.tools.system.package_manager import Apt

class QtTemplate(ConanFile):
    generators = 'CMakeToolchain', 'CMakeDeps'
    settings = 'os', 'arch', 'compiler', 'build_type'

    requires = 'fmt/9.0.0', 'qtbase/6.3.1@qt/everywhere'

    # def system_requirements(self):
        # apt = Apt(self, arch_names={'x86_64':'x86_64'})
        # apt.update()
        # apt.install(['git', 'vim', 'gcc', 'g++', 'cmake', 'ninja-build'])


    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)

        # Small hack. Add qt cmake path to conan toolchain for proper qt cmake files detection
        cmake_qt_root_path = path.normpath(self.deps_cpp_info['qtbase'].rootpath + '/lib/cmake')
        tc.blocks['find_paths'].values['host_build_paths_noroot'] = cmake_qt_root_path

        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
