# ctcms_workshop

These examples were generated using: 
python 3.9.7
psi4 1.5
critic2-1.1stable (https://aoterodelaroza.github.io/critic2/)

These slides and examples were prepared for a workshop discussion of SCF instability some of the causes, and possible solutions when working with DFT and other SCF methods. Please direct all questions to Stephen G. Dale https://scholar.google.com/citations?user=gS3ihw0AAAAJ&hl=en

01_default is a basic DFT calculation in psi4 chosen because it crashed with an SCF instability. [Note: newer versions of psi4 appear to fix this particular instability and a new example needs to be found.]

01_a/b changes the initial electron density guess of the SCF. 

02_example generates fchk files which are turned into cube files using gen_cubes.cri and critic2 so we can examine the change in electron density between SCF steps.

03_damping shows the damping technique, which mixed part of the previous SCF step with the current one to try and slow down changes in density and stabilise to a solution.

04_soscf shows second order convergence best conceptualised as following the second derivate, which we are using a Taylor expansion to find.

05_hf-guess uses a Hartree-Fock calculation as an initial guess. HF is generally more stable. This has been formalised in recent years as density-corrected DFT.

06_pcm uses a polarisable continuum model to stabilise the SCF. Note that this will start giving different chemistries as the PCM model is intended as a solvent correction, not as a stabiliser.

07_hf shows a stability analysis where an SCF solution is found, but it is actually a saddle point. The stability analysis routine then continues the minimization.
