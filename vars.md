## D_s vars

### kinematic vars

- C_Ds_pt = transverse momentum of the Ds candidate
- C_Ds_vertex_2DDist_BS = Ds vertex distance projection on transverse plane calculated wrt beam spot
- C_Ds_vertex_2DErr_BS = error on Ds vertex distance projection on transverse plane calculated wrt beam spotcalculated wrt primary vertex
- C_Ds_vertex_2DSig_BS = significance of Ds vertex distance projection on transverse plane calculated wrt beam spot
- C_Ds_vertex_cos2D = cosine of the Ds pointing angle (angle between flight direction and momentum) on the transverse plane
- C_Ds_vertex_cos3D = cosine of the Ds pointing angle (angle between flight direction and momentum)
- C_Ds_vertex_prob = Ds vertex fit probability

## HNL

### kinematic vars

- C_Hnl_pt = transverse momentum of the Hnl candidate
- C_Hnl_vertex_2DDist_BS = Hnl vertex distance projection on transverse plane calculated wrt beam spot
- C_Hnl_vertex_2DErr_BS = error on Hnl vertex distance projection on transverse plane calculated wrt beam spotcalculated wrt primary vertex
- C_Hnl_vertex_2DSig_BS = significance of Hnl vertex distance projection on transverse plane calculated wrt beam spot
- C_Hnl_vertex_cos2D = cosine of the Hnl pointing angle (angle between flight direction and momentum) on the transverse plane
- C_Hnl_vertex_cos3D = cosine of the Hnl pointing angle (angle between flight direction and momentum)
- C_Hnl_vertex_prob = Hnl vertex fit probability

## $D_s$ muon variables
### kinematic variables
- C_mu_Ds_BS_ip_xy = projection of Ds muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Ds_BS_ips_xy = significance of the projection of Ds muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Ds_phi = Ds muon phi
- C_mu_Ds_pt = Ds muon transverse momentum
- C_mu_Ds_eta = Ds muon eta
## HNL muon variables
### kinematic variables
- C_mu_Hnl_BS_ip_xy = projection of Hnl muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Hnl_BS_ips_xy = significance of the projection of Hnl muon impact parameter on transverse plane (calculated wrt beam spot)
- C_mu_Hnl_eta = Hnl muon eta
- C_mu_Hnl_phi = Hnl muon phi
- C_mu_Hnl_pt = Hnl muon transverse momentum

## $\pi$ variables
### kinematic variables
- C_pi_BS_ip_xy = projection of pi impact parameter on transverse plane (calculated wrt beam spot)
- C_pi_BS_ips_xy = significance of the projection of pi impact parameter on transverse plane (calculated wrt beam spot)
- C_pi_eta = pi eta
- C_pi_phi = pi phi
- C_pi_pt = pi transverse momentum
## $\Delta R$ variables
as is written explicitly, mu1 refers to HNL muon and mu2 to Ds muon
- C_mu1mu2_dr = $\Delta R \equiv \sqrt{\Delta \eta^2 + \Delta \phi^2}$ between the two muons
- C_mu1mu2_mass = mass difference between the two muons
- C_mu1pi_dr = $\Delta R \equiv \sqrt{\Delta \eta^2 + \Delta \phi^2}$ between HNL muon and the pion
- C_mu2pi_dr = $\Delta R \equiv \sqrt{\Delta \eta^2 + \Delta \phi^2}$ between Ds muon and the pion

## extras
- C_pass_gen_matching = matches with generator (only for signal)

## variables listed for code
~~~
C_Ds_pt 
C_Ds_vertex_2DDist_BS 
C_Ds_vertex_2DErr_BS 
C_Ds_vertex_2DSig_BS 
C_Ds_vertex_cos2D 
C_Ds_vertex_cos3D 
C_Ds_vertex_prob 
C_Hnl_pt 
C_Hnl_vertex_2DDist_BS 
C_Hnl_vertex_2DErr_BS 
C_Hnl_vertex_2DSig_BS 
C_Hnl_vertex_cos2D 
C_Hnl_vertex_cos3D 
C_Hnl_vertex_prob 
C_mu_Ds_BS_ip_xy 
C_mu_Ds_BS_ips_xy 
C_mu_Ds_phi 
C_mu_Ds_pt 
C_mu_Ds_eta 
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
C_mu1mu2_dr 
C_mu1mu2_mass 
C_mu1pi_dr  
C_mu2pi_dr  
C_pass_gen_matching 
~~~