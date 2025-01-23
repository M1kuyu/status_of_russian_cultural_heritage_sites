
import React, { useEffect, useState } from "react";
import { fetchHeritageSites } from "../api/heritageSites";

const DisplayHeritageSites = () => {
    const [sites, setSites] = useState([]);

    useEffect(() => {
        const loadSites = async () => {
            const data = await fetchHeritageSites();
            setSites(data);
        };
        loadSites();
    }, []);

    return (
        <div>
            <h1>Cultural Heritage Sites</h1>
            <ul>
                {sites.map((site) => (
                    <li key={site.id}>
                        {site.ObjectName} - {site.Location}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DisplayHeritageSites;

