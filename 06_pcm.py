import psi4

n = "SSI-084TYR-089ASP-1-dimer"
Basis = "def2-msvp"

psi4.set_options({"basis": Basis,
                  "reference":"uks",
                  "pcm":True, 
                  "pcm_scf_type":'total'})

pcm_string = '''
            Units = Angstrom
            Medium {
            SolverType = cpcm
            Solvent = Explicit
            ProbeRadius=2.0
            Green<inside> {Type=Vacuum}
            Green<outside> {Type=UniformDielectric
                            Eps=80
                            EpsDyn=2.0}
            }
            Cavity {
            RadiiSet = UFF
            Type = GePol
            Scaling = False
            Area = 0.3
            Mode = Implicit
            }
        '''

psi4.pcm_helper(pcm_string)

xyz = "".join(open(f'./{n}.xyz', 'r').readlines()[1:])
xyz = psi4.geometry(xyz)
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)
