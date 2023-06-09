Field_name = {
    "systemname": "SystemName",
    "systemLabel": "SystemLabel",
MPI.Nprocs.SIESTA         8     # default value
SpinPolarized              F     # default value
NonCollinearSpin              F     # default value
SpinOrbit              F     # default value
#:block? SpinPolarized              F
#:defined? SpinPolarized              F
#:block? NonCollinearSpin              F
#:defined? NonCollinearSpin              F
#:block? SpinOrbit              F
#:defined? SpinOrbit              F
Spin     none                                 # default value
TimeReversalSymmetry              T     # default value
DebugObjects.Node         0     # default value
DebugObjects              F     # default value
XML.Write              F     # default value
timer_report_threshold          0.000000000         # default value
UseParallelTimer              T     # default value
UseTreeTimer              F     # default value
alloc_report_level         0     # default value
alloc_report_threshold          0.000000000         # default value
xc.functional     GGA                                                                             
xc.authors     PBE                                                                             
MM.Cutoff          30.00000000     Bohr     # default value
MM.UnitsEnergy     eV     # default value
MM.UnitsDistance     Ang     # default value
WriteIonPlotFiles              F     # default value
Atom.Debug.KB.Generation              F     # default value
KB.New.Reference.Orbitals              F     # default value
user-basis              F     # default value
user-basis-netcdf              F     # default value
#:block? LDAU.proj              F
#:defined? LDAU.proj              F
Number_of_species              1
%block Chemical_species_label
  1 14 Si # NRGGA
%endblock Chemical_species_label
ReparametrizePseudos              F     # default value
Restricted.Radial.Grid              T     # default value
Rmax.Radial.Grid          0.000000000         # default value
PAO.BasisSize     standard            # default value
PAO.BasisType     split          # default value
PAO.SoftDefault              F     # default value
PAO.SoftInnerRadius         0.9000000000         # default value
PAO.SoftPotential          40.00000000         # default value
PAO.SplitNorm         0.1500000000         # default value
PAO.SplitNormH         -1.000000000         # default value
LDAU.ProjectorGenerationMethod         2     # default value
LDAU.EnergyShift         0.5000000000E-01 Ry     # default value
LDAU.CutoffNorm         0.9000000000         # default value
PAO.SoftDefault              F     # default value
PAO.SoftInnerRadius         0.9000000000         # default value
PAO.SoftPotential          40.00000000         # default value
LDAU.ThresholdTol         0.1000000000E-01     # default value
LDAU.PopTol         0.1000000000E-02     # default value
LDAU.PotentialShift              F     # default value
LDAU.FirstIteration              F     # default value
FilterCutoff          0.000000000     Ry     # default value
FilterTol          0.000000000     Ry     # default value
KB.Rmax          6.000000000     Bohr     # default value
PAO.EnergyShift         0.1000000000E-01         Ry
# above item originally: PAO.EnergyShift         0.1000000000E-01 Ry        
PAO.SplitTailNorm              F     # default value
PAO.FixSplitTable              F     # default value
PAO.NewSplitCode              F     # default value
PAO.Filter              F     # default value
PAO.Keep.Findp.Bug              F     # default value
PAO.Filter              F     # default value
PAO.Filter              F     # default value
PAO.Filter              F     # default value
PAO.OldStylePolorbs              T     # default value
PAO.SplitTailNorm              F     # default value
PAO.FixSplitTable              F     # default value
PAO.NewSplitCode              F     # default value
PAO.Filter              F     # default value
Vna.Filter              F     # default value
PAO.BasisType     split          # default value
Atom-Setup-Only              F     # default value
UseStructFile              F     # default value
MD.UseStructFile              F     # default value
LatticeConstant          10.26121695           Bohr
# above item originally: LatticeConstant          5.430000000     Ang       
#:block? LatticeParameters              F
#:block? LatticeVectors              T
%block LatticeVectors
     	 1.000000    0.000000    0.000000
          0.000000    1.000000    0.000000
          0.000000    0.000000    1.000000
%endblock LatticeVectors
%block SuperCell
 1 0 0
 0 1 0
 0 0 1
%endblock SuperCell
AtomicCoordinatesFormat     ScaledCartesian                                                                 
NumberOfAtoms              8
ZM.UnitsLength     Bohr           # default value
ZM.UnitsAngle     rad            # default value
ZM.ForceTolLength         0.1555740000E-02 Ry/Bohr     # default value
ZM.ForceTolAngle         0.3565490000E-02 Ry/rad     # default value
ZM.MaxDisplLength         0.2000000000     Bohr     # default value
ZM.MaxDisplAngle         0.3000000000E-02 rad     # default value
ZM.CalcAllForces              F     # default value
%block AtomicCoordinatesAndAtomicSpecies
 0.00    0.00    0.00  1
 0.50    0.50    0.00  1
 0.50    0.00    0.50  1
 0.00    0.50    0.50  1
 0.25    0.25    0.25  1
 0.25    0.75    0.75  1
 0.75    0.25    0.75  1
 0.75    0.75    0.25  1
%endblock AtomicCoordinatesAndAtomicSpecies
MD.UseSaveXV              F
MD.UseSaveZM              F     # default value
WriteCoorInitial              T
MD.TypeOfRun     CG                                                                              
MaxBondDistance          6.000000000     Bohr     # default value
LatticeConstant          10.26121695           Bohr
# above item originally: LatticeConstant          5.430000000     Ang       
Output-Structure-Only              F     # default value
WriteCoorXmol              T
#:physical? MaxWalltime              F
MaxWalltime         0.1797693135+309     # default value
#:physical? MaxWalltime.Slack              F
MaxWalltime.Slack          5.000000000         # default value
HSetupOnly              F     # default value
LongOutput              F     # default value
WriteDenchar              F     # default value
WriteMullikenPop         0     # default value
WriteOrbMom              F     # default value
WriteHirshfeldPop              F     # default value
WriteVoronoiPop              F     # default value
PartialChargesAtEveryGeometry              F     # default value
PartialChargesAtEveryScfStep              F     # default value
Compat.Matel.NRTAB              F     # default value
MeshCutoff          200.0000000             Ry
# above item originally: MeshCutoff          200.0000000     Ry        
NetCharge          0.000000000         # default value
MinSCFIterations         0     # default value
MaxSCFIterations            300
SCF.MustConverge              T     # default value
#:block? TS.MixH              F
#:defined? TS.MixH              F
#:block? MixHamiltonian              F
#:defined? MixHamiltonian              F
#:block? MixCharge              F
#:defined? MixCharge              F
TS.MixH              T     # default value
MixHamiltonian              T     # default value
MixCharge              F     # default value
SCF.Mix     Hamiltonian     # default value
Compat-pre-v4-DM-H              F     # default value
SCF.MixAfterConvergence              F     # default value
SCF.Recompute-H-After-Scf              F     # default value
DM.NumberPulay              3
DM.NumberBroyden         0     # default value
DM.FIRE.Mixing              F     # default value
DM.MixSCF1              T     # default value
SCF.Mix.First              T     # default value
DM.PulayOnFile              F     # default value
DM.MixingWeight         0.5000000000    
DM.OccupancyTolerance         0.1000000000E-11     # default value
DM.NumberKick         0     # default value
DM.KickMixingWeight         0.5000000000         # default value
DM.RequireHarrisConvergence              F     # default value
SCF.Harris.Converge              F     # default value
DM.HarrisTolerance         0.7349806700E-05 Ry     # default value
SCF.Harris.Tolerance         0.7349806700E-05 Ry     # default value
SCF.DM.Converge              T     # default value
DM.Tolerance         0.1000000000E-03     # default value
SCF.DM.Tolerance         0.1000000000E-03     # default value
SCF.EDM.Converge              F     # default value
SCF.EDM.Tolerance         0.7349806700E-04 Ry     # default value
SCF.H.Converge              T     # default value
SCF.H.Tolerance         0.7349806700E-04 Ry     # default value
DM.RequireEnergyConvergence              F     # default value
SCF.FreeE.Converge              F     # default value
DM.EnergyTolerance         0.7349806700E-05 Ry     # default value
SCF.FreeE.Tolerance         0.7349806700E-05 Ry     # default value
MonitorForcesInSCF              F     # default value
SCF.MonitorForces              F     # default value
UseSaveData              F     # default value
DM.UseSaveDM              F
NeglNonOverlapInt              F     # default value
SolutionMethod     Diagon                                                                          
ElectronicTemperature         0.1900069269E-02         Ry
# above item originally: ElectronicTemperature          300.0000000     K         
FixSpin              F     # default value
Spin.Fix              F     # default value
ON.MaxNumIter      1000     # default value
ON.etol         0.1000000000E-07     # default value
ON.eta          0.000000000     Ry     # default value
ON.eta_alpha          0.000000000     Ry     # default value
ON.eta_beta          0.000000000     Ry     # default value
On.RcLWF          9.500000000     Bohr     # default value
ON.UseSaveLWF              F     # default value
ON.functional     kim     # default value
ON.ChemicalPotentialUse              F     # default value
ON.ChemicalPotential              F     # default value
ON.ChemicalPotentialRc          9.500000000     Bohr     # default value
ON.ChemicalPotentialTemperature         0.5000000000E-01 Ry     # default value
ON.ChemicalPotentialOrder       100     # default value
MD.VariableCell              F
compat-pre-v4-dynamics              F     # default value
MD.TypeOfRun     CG                                                                              
MD.UseSaveCG              F
Optim.Broyden              F     # default value
#:block? Optim.Broyden              F
#:defined? Optim.Broyden              F
MD.NumCGsteps              0
MD.Steps         0     # default value
MD.MaxCGDispl         0.1000000000           Bohr
# above item originally: MD.MaxCGDispl         0.1000000000     Bohr      
MD.MaxDispl         0.1000000000     Bohr     # default value
MD.MaxForceTol         0.1555739508E-02    Ry/Bohr
# above item originally: MD.MaxForceTol         0.4000000000E-01 eV/Ang    
MD.MaxStressTol         0.6797730000E-04 Ry/Bohr**3     # default value
GeometryMustConverge              F     # default value
MD.InitialTimeStep         1     # default value
#:block? MD.Steps              F
#:defined? MD.Steps              F
MD.FinalTimeStep         1     # default value
MD.LengthTimeStep          1.000000000     fs     # default value
MD.Quench              F     # default value
MD.FireQuench              F     # default value
MD.InitialTemperature          0.000000000     K     # default value
MD.TargetTemperature          0.000000000     K     # default value
MD.TargetPressure          0.000000000     Ry/Bohr**3     # default value
MD.NoseMass          100.0000000     Ry*fs**2     # default value
MD.ParrinelloRahmanMass          100.0000000     Ry*fs**2     # default value
MD.AnnealOption     TemperatureAndPressure     # default value
MD.TauRelax          100.0000000     fs     # default value
MD.BulkModulus         0.6797730000E-02 Ry/Bohr**3     # default value
MD.FCDispl         0.4000000000E-01 Bohr     # default value
MD.FCfirst         1     # default value
MD.FClast         8     # default value
UseSpatialDecomposition              F     # default value
UseDomainDecomposition              F     # default value
SCF.Mix.Spin     all     # default value
Mixer.Debug              F     # default value
Mixer.Debug.MPI              F     # default value
DM.NumberPulay              3
DM.NumberBroyden         0     # default value
DM.MixingWeight         0.5000000000    
DM.NumberKick         0     # default value
DM.KickMixingWeight         0.5000000000         # default value
SCF.LinearMixingAfterPulay              F     # default value
SCF.MixingWeightAfterPulay         0.5000000000         # default value
SCF.Mixer.History         3     # default value
SCF.Mixer.Weight         0.5000000000         # default value
SCF.Mixer.Kick         0     # default value
SCF.Mixer.Kick.Weight         0.5000000000         # default value
SCF.Mixer.Restart         0     # default value
SCF.Mixer.Restart.Save         1     # default value
SCF.Mixer.Method     Pulay     # default value
SCF.Mixer.Variant     original     # default value
SCF.Mixer.Linear.After        -1     # default value
SCF.Mixer.Linear.After.Weight         0.5000000000         # default value
#:block? ChargeGeometries              F
#:defined? ChargeGeometries              F
#:block? ChargeGeometries              F
#:defined? ChargeGeometries              F
Harris_functional              F     # default value
ForceAuxCell              F     # default value
#:block? Optim.Broyden.History.Steps              F
#:defined? Optim.Broyden.History.Steps              F
#:block? Optim.Broyden.Cycle.On.Maxit              F
#:defined? Optim.Broyden.Cycle.On.Maxit              F
#:block? Optim.Broyden.Variable.Weight              F
#:defined? Optim.Broyden.Variable.Weight              F
#:block? Optim.Broyden.Debug              F
#:defined? Optim.Broyden.Debug              F
#:block? Optim.Broyden.Initial.Inverse.Jacobian              F
#:defined? Optim.Broyden.Initial.Inverse.Jacobian              F
WriteKpoints              F     # default value
WriteForces              F     # default value
WriteDM              T     # default value
WriteDM.End.Of.Cycle              T     # default value
WriteH              F     # default value
WriteH.End.Of.Cycle              F     # default value
WriteDM.NetCDF              F     # default value
WriteDM.History.NetCDF              F     # default value
WriteDMHS.NetCDF              T
WriteDMHS.History.NetCDF              F     # default value
SCF.Read.Charge.NetCDF              F     # default value
SCF.Read.Deformation.Charge.NetCDF              F     # default value
Write.TSHS.History              F     # default value
SaveInitialChargeDensity              F     # default value
AnalyzeChargeDensityOnly              F     # default value
UseNewDiagk              F     # default value
WriteBands              T
WriteKbands              F     # default value
WriteEigenvalues              F     # default value
WriteCoorStep              T
WriteMDhistory              F     # default value
WriteMDXmol              T
WriteOrbitalIndex              T     # default value
Write.Graphviz     none     # default value
WriteCoorStep              T
SaveHS              T
ReInitialiseDM              T     # default value
DM.AllowReuse              T     # default value
DM.AllowExtrapolation              T     # default value
DM.History.Depth         1     # default value
DM.NormalizationTolerance         0.1000000000E-04     # default value
DM.NormalizeDuringSCF              T     # default value
MullikenInSCF              F     # default value
SpinInSCF              F     # default value
WarningMinimumAtomicDistance          1.000000000     Bohr     # default value
BornCharge              F     # default value
ChangeKgridInMD              F     # default value
MD.RelaxCellOnly              F     # default value
MD.RemoveIntraMolecularPressure              F     # default value
COOP.Write              F     # default value
SaveRho              T
SaveDeltaRho              F     # default value
SaveRhoXC              F     # default value
SaveElectrostaticPotential              T
SaveNeutralAtomPotential              F     # default value
SaveTotalPotential              F     # default value
SaveIonicCharge              F     # default value
SaveBaderCharge              F     # default value
SaveTotalCharge              F     # default value
Siesta2Wannier90.WriteMmn              F     # default value
Siesta2Wannier90.WriteUnk              F     # default value
Siesta2Wannier90.WriteAmn              F     # default value
Siesta2Wannier90.WriteEig              F     # default value
#:block? Siesta2Wannier90.NumberOfBandsUp              F
#:defined? Siesta2Wannier90.NumberOfBandsUp              F
#:block? Siesta2Wannier90.NumberOfBandsDown              F
#:defined? Siesta2Wannier90.NumberOfBandsDown              F
#:block? Siesta2Wannier90.NumberOfBands              F
#:defined? Siesta2Wannier90.NumberOfBands              F
Siesta2Wannier90.NumberOfBandsUp         0     # default value
Siesta2Wannier90.NumberOfBandsDown         0     # default value
Siesta2Wannier90.NumberOfBands         0     # default value
DM.AllowReuse              T     # default value
DM.AllowExtrapolation              T     # default value
DM.AllowExtrapolation              F     # default value
RcSpatial          0.000000000     Bohr     # default value
ProcessorGridX         1     # default value
ProcessorGridY         1     # default value
ProcessorGridZ         1     # default value
processorY         2     # default value
blocksize        13     # default value
NumberOfEigenStates       104     # default value
#:block? SpinSpiral              F
#:defined? SpinSpiral              F
TimeReversalSymmetryForKpoints              T     # default value
%block kgrid_Monkhorst_Pack
   4  0  0  0.5
   0  4  0  0.5
   0  0  4  0.5
%endblock kgrid_Monkhorst_Pack
Diag.ParallelOverK              F     # default value
Diag.ProcessorY         2     # default value
Diag.BlockSize        13     # default value
Diag.Use2D              T     # default value
Diag.UpperLower     lower     # default value
Diag.DivideAndConquer              T     # default value
Diag.NoExpert              F     # default value
Diag.Algorithm     Divide-and-Conquer     # default value
Diag.AbsTol         0.1000000000E-15     # default value
Diag.OrFac         0.1000000000E-05     # default value
Diag.Memory          1.000000000         # default value
#:block? ProjectedDensityOfStates              T
#:block? SpinSpiral              F
#:defined? SpinSpiral              F
TimeReversalSymmetryForKpoints              T     # default value
%block PDOS.kgrid_Monkhorst_Pack
 12   0   0  0.0
 0   12   0  0.0
 0   0   12  0.0
%endblock PDOS.kgrid_Monkhorst_Pack
#:block? BandLines              T
#:defined? BandLines              T
#:block? BandPoints              F
#:defined? BandPoints              F
BandLinesScale     ReciprocalLatticeVectors                                                        
%block BandLines
 1	0.5	0.5	0.5	L
 100	0.0	0.0	0.0	G
 100	0.5	0.0	0.5	X
%endblock BandLines
#:block? BandLines              T
#:defined? BandLines              T
#:block? BandPoints              F
#:defined? BandPoints              F
BandLinesScale     ReciprocalLatticeVectors                                                        
%block BandLines
 1	0.5	0.5	0.5	L
 100	0.0	0.0	0.0	G
 100	0.5	0.0	0.5	X
%endblock BandLines
LongOutput              F     # default value
WriteWaveFunctions              F     # default value
#:block-line-count? MetaForce (iirrr)   0
#:block? TS.BufferAtomsLeft              F
#:defined? TS.BufferAtomsLeft              F
#:block? TS.BufferAtomsRight              F
#:defined? TS.BufferAtomsRight              F
#:list? TS.Atoms.Buffer              F
TS.HS.Save              F     # default value
TS.DE.Save              F     # default value
TS.onlyS              F     # default value
TS.S.Save              F     # default value
AtomicCoordinatesFormat     ScaledCartesian                                                                 
AtomCoorFormatOut     ScaledCartesian            # default value
LatticeConstant          10.26121695           Bohr
# above item originally: LatticeConstant          5.430000000     Ang       
debug-folding              F     # default value
Sonly              F     # default value
Sonly              F     # default value
Debug.DHSCF              F     # default value
MeshSubDivisions         2     # default value
PROCS_PER_NODE         4     # default value
PROCS_PER_NODE         4     # default value
DirectPhi              F     # default value
SimulateDoping              F     # default value
Read-H-from-file              F     # default value
SingleExcitation              F     # default value
OccupationFunction     FD     # default value
OccupationFunction     FD     # default value
compute-forces              T     # default value
#:list? Grid.CellSampling              F
Read-H-from-file              F     # default value
WriteCoorXmol              T
WriteCoorCerius              F     # default value
WFS.Write.For.Bands              F     # default value
%block ProjectedDensityOfStates
    -10.00  10.00  0.03  500 eV
%endblock ProjectedDensityOfStates
BasisPressure         0.2000000000     GPa     # default value
OpticalCalculation              F     # default value


    }


