from setuptools import setup

setup(
    name='Keep or Skip',
    version='0.1.0',    
    description='Tinder like image sorter!',
    url='',
    author='2sleepy4u',
    author_email='riccardo.zancan00@gmail.com',
    license='BSD 2-clause',
    packages=['skeep'],
    install_requires=[ 
        "pygame",
    ],
    entry_points={
        'console_scripts': [
            'skeep=skeep.main:main',  # Adjust as needed
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
