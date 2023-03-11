import psi4

n = "SSI-084TYR-089ASP-1-dimer"
Basis = "def2-msvp"

xyz = "".join(open(f'./{n}.xyz', 'r').readlines()[1:])
xyz = psi4.geometry(xyz)
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)

psi4.set_options({"basis": Basis,
                  "reference":"uks",
                  "fail_on_maxiter":False,
                  "maxiter":5,
                  "guess":"sad"})
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)
psi4.fchk(wfn, "5.fchk")

psi4.set_options({"basis": Basis,
                  "reference":"uks",
                  "fail_on_maxiter":False,
                  "maxiter":6,
                  "guess":"sad"})
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)
psi4.fchk(wfn, "6.fchk")

psi4.set_options({"basis": Basis,
                  "reference":"uks",
                  "fail_on_maxiter":False,
                  "maxiter":7,
                  "guess":"sad"})
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)
psi4.fchk(wfn, "7.fchk")

psi4.set_options({"basis": Basis,
                  "reference":"uks",
                  "fail_on_maxiter":False,
                  "maxiter":8,
                  "guess":"sad"})
e, wfn = psi4.energy('pbe', molecule=xyz, return_wfn=True)
psi4.fchk(wfn, "8.fchk")
