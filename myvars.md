## $D_s$ and HNL

### $D_s$ variables

#### kinematic variables
- C_Ds_mass = Mass of the Ds candidate
- C_Ds_pt = transverse momentum of the Ds candidate
- C_Ds_px = x momentum component of the Ds candidate
- C_Ds_py = y momentum component of the Ds candidate
- C_Ds_pz = z momentum component of the Ds candidate
- C_Ds_vertex_2DDist_BS = Ds vertex distance projection on transverse plane calculated wrt beam spot
- C_Ds_vertex_2DDist_PV = Ds vertex distance projection on transverse plane calculated wrt primary vertex
- C_Ds_vertex_2DErr_BS = error on Ds vertex distance projection on transverse plane calculated wrt beam spot
- C_Ds_vertex_2DErr_PV = error on Ds vertex distance projection on transverse plane calculated wrt primary vertex
- C_Ds_vertex_2DSig_BS = significance of Ds vertex distance projection on transverse plane calculated wrt beam spot
- C_Ds_vertex_2DSig_PV = significance of Ds vertex distance projection on transverse plane calculated wrt primary vertex
- C_Ds_vertex_3DDist_BS = Ds vertex distance calculated wrt beam spot
- C_Ds_vertex_3DDist_PV = Ds vertex distance calculated wrt primary vertex
- C_Ds_vertex_3DErr_BS = error on Ds vertex distance calculated wrt beam spot
- C_Ds_vertex_3DErr_PV = error on Ds vertex distance calculated wrt primary vertex
- C_Ds_vertex_3DSig_BS = significance of Ds vertex distance calculated wrt beam spot
- C_Ds_vertex_3DSig_PV = significance of Ds vertex distance calculated wrt primary vertex
- C_Ds_vertex_cos2D = cosine of the Ds pointing angle (angle between flight direction and momentum) on the transverse plane
- C_Ds_vertex_cos3D = cosine of the Ds pointing angle (angle between flight direction and momentum)
- C_Ds_vertex_prob = Ds vertex fit probability
- C_Ds_vertex_x = Ds reconstructed vertex position on x
- C_Ds_vertex_xErr = error on Ds reconstructed vertex position on x
- C_Ds_vertex_y = Ds reconstructed vertex position on y
- C_Ds_vertex_yErr = error on Ds reconstructed vertex position on y
- C_Ds_vertex_z = Ds reconstructed vertex position on y
- C_Ds_vertex_zErr = error on Ds reconstructed vertex position on y

### HNL variables
#### kinematic variables

- C_Hnl_gen_l = generator level HNL decay length
- C_Hnl_gen_l_prop = generator level HNL proper decay length
- C_Hnl_mass = Mass of the Hnl candidate
- C_Hnl_pt = transverse momentum of the Hnl candidate
- C_Hnl_px = x momentum component of the Hnl candidate
- C_Hnl_py = y momentum component of the Hnl candidate
- C_Hnl_pz = z momentum component of the Hnl candidate
- C_Hnl_vertex_2DDist_BS = Hnl vertex distance projection on transverse plane calculated wrt beam spot
- C_Hnl_vertex_2DDist_PV = Hnl vertex distance projection on transverse plane calculated wrt primary vertex
- C_Hnl_vertex_2DErr_BS = error on Hnl vertex distance projection on transverse plane calculated wrt beam spot
- C_Hnl_vertex_2DErr_PV = error on Hnl vertex distance projection on transverse plane calculated wrt primary vertex
- C_Hnl_vertex_2DSig_BS = significance of Hnl vertex distance projection on transverse plane calculated wrt beam spot
- C_Hnl_vertex_2DSig_PV = significance of Hnl vertex distance projection on transverse plane calculated wrt primary vertex
- C_Hnl_vertex_3DDist_BS = Hnl vertex distance calculated wrt beam spot
- C_Hnl_vertex_3DDist_PV = Hnl vertex distance calculated wrt primary vertex
- C_Hnl_vertex_3DErr_BS = error on Hnl vertex distance calculated wrt beam spot
- C_Hnl_vertex_3DErr_PV = error on Hnl vertex distance calculated wrt primary vertex
- C_Hnl_vertex_3DSig_BS = significance of Hnl vertex distance calculated wrt beam spot
- C_Hnl_vertex_3DSig_PV = significance of Hnl vertex distance calculated wrt primary vertex
- C_Hnl_vertex_cos2D = cosine of the Hnl pointing angle (angle between flight direction and momentum) on the transverse plane
- C_Hnl_vertex_cos3D = cosine of the Hnl pointing angle (angle between flight direction and momentum)
- C_Hnl_vertex_prob = Hnl vertex fit probability
- C_Hnl_vertex_x = Hnl reconstructed vertex position on x
- C_Hnl_vertex_xErr = error on Hnl reconstructed vertex position on x
- C_Hnl_vertex_y = Hnl reconstructed vertex position on y
- C_Hnl_vertex_yErr = error on Hnl reconstructed vertex position on y
- C_Hnl_vertex_z = Hnl reconstructed vertex position on y
- C_Hnl_vertex_zErr = error on Hnl reconstructed vertex position on y

## cross-related variables
as is written explicitly, mu1 refers to HNL muon and mu2 to Ds muon
- C_mu1mu2_dr = $\Delta R \equiv \sqrt{\Delta \eta^2 + \Delta \phi^2}$ between the two muons
- C_mu1mu2_mass = mass difference between the two muons
- C_mu1pi_dr = $\Delta R \equiv \sqrt{\Delta \eta^2 + \Delta \phi^2}$ between HNL muon and the pion
- C_mu2pi_dr = $\Delta R \equiv \sqrt{\Delta \eta^2 + \Delta \phi^2}$ between Ds muon and the pion

## $D_s$ muon variables
### kinematic variables
- C_mu_Ds_BS_ip_xy = projection of Ds muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Ds_BS_ips_xy = significance of the projection of Ds muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Ds_BS_x = Ds muon vertex position along x (seems to be constant?)
- C_mu_Ds_BS_y = Ds muon vertex position along y (seems to be constant?)
- C_mu_Ds_BS_z = Ds muon vertex position along z
- C_mu_Ds_PV_* = same as C_mu_Ds_BS_* variables but calculated wrt primary vertex
- C_mu_Ds_eta = Ds muon eta
- C_mu_Ds_fitted_E = Ds muon energy (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Ds_fitted_px = Ds muon momentum along x (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Ds_fitted_py = Ds muon momentum along y (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Ds_fitted_pz = Ds muon momentum along z (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Ds_phi = Ds muon phi
- C_mu_Ds_pt = Ds muon transverse momentum
### discrete/boolean variables
- C_mu_Ds_charge = Ds muon charge
- C_mu_Ds_iBestPV = index of associated PV
- C_mu_Ds_idx = index of associated muon in MINIAOD 
- C_mu_Ds_isGlobal = Ds muon is a global muon
- C_mu_Ds_isLoose = Ds muon pass loose id
- C_mu_Ds_isMedium = Ds muon pass medium id
- C_mu_Ds_isSoft = Ds muon pass soft id
- C_mu_Ds_isStandAlone = Ds muon is a standalone muon
- C_mu_Ds_isTracker = Ds muon is a tracker muon

## HNL muon variables

### kinematic variables
- C_mu_Hnl_BS_ip_xy = projection of Hnl muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Hnl_BS_ips_xy = significance of the projection of Hnl muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Hnl_PV_* = same as C_mu_Hnl_BS_* variables but calculated wrt primary vertex
- C_mu_Hnl_eta = Hnl muon eta
- C_mu_Hnl_fitted_E = Hnl muon energy (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Hnl_fitted_px = Hnl muon momentum along x (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Hnl_fitted_py = Hnl muon momentum along y (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Hnl_fitted_pz = Hnl muon momentum along z (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_mu_Hnl_phi = Hnl muon phi
- C_mu_Hnl_pt = Hnl muon transverse momentum
### discrete/boolean variables
- C_mu_Hnl_charge = Hnl muon charge
- C_mu_Hnl_iBestPV = index of associated PV
- C_mu_Hnl_idx = index of associated muon in MINIAOD 
- C_mu_Hnl_isGlobal = Hnl muon is a global muon
- C_mu_Hnl_isLoose = Hnl muon pass loose id
- C_mu_Hnl_isMedium = Hnl muon pass medium id
- C_mu_Hnl_isSoft = Hnl muon pass soft id
- C_mu_Hnl_isStandAlone = Hnl muon is a standalone muon
- C_mu_Hnl_isTracker = Hnl muon is a tracker muon

## $\pi$ variables
### kinematic variables
- C_pi_BS_ip_xy = projection of pi impact parameter on transverse plane (calculated wrt beam spot)
- C_pi_BS_ips_xy = significance of the projection of pi impact parameter on transverse plane (calculated wrt beam spot)
- C_pi_PV_* = same as C_pi_BS_* variables but calculated wrt primary vertex
- C_pi_eta = pi eta
- C_pi_fitted_E = pi energy (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_pi_fitted_px = pi momentum along x (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_pi_fitted_py = pi momentum along y (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_pi_fitted_pz = pi momentum along z (from kinematic fit) (\# fitted variables seem to have some issues, do not use)
- C_pi_phi = pi phi
- C_pi_pt = pi transverse momentum
### discrete/boolean variables
- C_pi_charge = pi charge
- C_pi_iBestPV = index of associated PV
- C_pi_idx = index of associated muon in MINIAOD 
- C_pi_isGlobal = pi is a global muon
- C_pi_isLoose = pi pass loose id
- C_pi_isMedium = pi pass medium id
- C_pi_isSoft = pi pass soft id
- C_pi_isStandAlone = pi is a standalone muon
- C_pi_isTracker = π is a tracker muon

## extras
- C_pass_gen_matching = matches with generator (only for signal)

## kinematic variables listed for code
~~~
C_Ds_mass  
C_Ds_pt  
C_Ds_px  
C_Ds_py  
C_Ds_pz  
C_Ds_vertex_2DDist_BS  
C_Ds_vertex_2DDist_PV  
C_Ds_vertex_2DErr_BS  
C_Ds_vertex_2DErr_PV  
C_Ds_vertex_2DSig_BS  
C_Ds_vertex_2DSig_PV  
C_Ds_vertex_3DDist_BS  
C_Ds_vertex_3DDist_PV  
C_Ds_vertex_3DErr_BS  
C_Ds_vertex_3DErr_PV  
C_Ds_vertex_3DSig_BS  
C_Ds_vertex_3DSig_PV  
C_Ds_vertex_cos2D  
C_Ds_vertex_cos3D  
C_Ds_vertex_prob  
C_Ds_vertex_x  
C_Ds_vertex_xErr  
C_Ds_vertex_y  
C_Ds_vertex_yErr  
C_Ds_vertex_z  
C_Ds_vertex_zErr  
C_Hnl_mass  
C_Hnl_pt  
C_Hnl_px  
C_Hnl_py  
C_Hnl_pz  
C_Hnl_vertex_2DDist_BS  
C_Hnl_vertex_2DDist_PV  
C_Hnl_vertex_2DErr_BS  
C_Hnl_vertex_2DErr_PV  
C_Hnl_vertex_2DSig_BS  
C_Hnl_vertex_2DSig_PV  
C_Hnl_vertex_3DDist_BS  
C_Hnl_vertex_3DDist_PV  
C_Hnl_vertex_3DErr_BS  
C_Hnl_vertex_3DErr_PV  
C_Hnl_vertex_3DSig_BS  
C_Hnl_vertex_3DSig_PV  
C_Hnl_vertex_cos2D  
C_Hnl_vertex_cos3D  
C_Hnl_vertex_prob  
C_Hnl_vertex_x  
C_Hnl_vertex_xErr  
C_Hnl_vertex_y  
C_Hnl_vertex_yErr  
C_Hnl_vertex_z  
C_Hnl_vertex_zErr  
C_mu_Ds_BS_ip_xy  
C_mu_Ds_BS_ips_xy  
C_mu_Ds_BS_x  
C_mu_Ds_BS_y  
C_mu_Ds_BS_z  
C_mu_Ds_eta
C_mu_Ds_phi  
C_mu_Ds_pt  
C_mu_Hnl_BS_ip_xy  
C_mu_Hnl_BS_ips_xy    
C_mu_Hnl_eta 
C_mu_Hnl_phi  
C_mu_Hnl_pt  
C_pi_BS_ip_xy  
C_pi_BS_ips_xy
C_pi_eta
C_pi_phi  
C_pi_pt  
~~~