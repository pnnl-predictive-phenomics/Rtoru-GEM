from distutils.core import setup


def main():
    setup(name='rtoru',
          version='1.0',
          description='Rhodosporidium Toruloides Ifo 08804',
          author='?',
          author_email='?',
          packages=['rtoru'],
          requires=['cobra'],
          keywords=['systems', 'biology', 'model', 'rules'],
          classifiers=[
            'Intended Audience :: Science/Research',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Mathematics',
            ],
          )


if __name__ == '__main__':
    main()