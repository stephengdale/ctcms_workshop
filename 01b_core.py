import psi4

n = "SSI-084TYR-089ASP-1-dimer"
Basis = "def2-msvp"

psi4.set_options({"basis": Basis,
                  "reference":"uks",
                  "guess":"core"})
# psi4.set_output_file(f"{n}.out")
xyz = "".join(open(f'./{n}.xyz', 'r').readlines()[1:])
xyz = psi4.geometry(xyz)
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)
