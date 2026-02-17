import pandapipes as pp

def simulate_hour(demand_kg_s, temp_k=350, pressure_bar=5):
    net = pp.create_empty_network(fluid="water")

    j1 = pp.create_junction(net, pn_bar=pressure_bar, tfluid_k=temp_k)
    j2 = pp.create_junction(net, pn_bar=pressure_bar, tfluid_k=temp_k)

    pp.create_pipe_from_parameters(
        net,
        from_junction=j1,
        to_junction=j2,
        length_km=0.1,
        diameter_m=0.1,
        k_mm=0.1
    )

    pp.create_ext_grid(net, junction=j1, p_bar=pressure_bar, t_k=temp_k)
    pp.create_sink(net, junction=j2, mdot_kg_per_s=demand_kg_s)

    pp.pipeflow(net)

    result = {
        "pressure_at_consumer": float(net.res_junction.p_bar.iloc[1]),
        "mass_flow": float(net.res_pipe["mdot_to_kg_per_s"].iloc[0])
    }

    return result
