### TODO: 
  - try mounting persistent volumes - Done:
    - done via pv & pvc using host Directory 
    - also tried downward API to expose pod & container meta-data

  - try to connect to a cloud DB:
    - not specific to kubernetes unless network policies restrict outbound network. 
    - work with network policies & egress to acheive this 

  - understand and incorporate nginx into the project

### TODO 5th June: 
    - Use a StatefulSet (1 replica for single DB) + PersistentVolumeClaim(s).
    - Expose with a ClusterIP Service for internal access.
    - Store credentials in a Secret and mount them as env vars.
    - Use readiness/liveness probes and resource limits.

There are dozens of Kubernetes resources. The easiest way to see everything supported by your cluster is:

bash: kubectl api-resources

The most important built-in resources are:

### Workload Resources

* `Pod`
* `ReplicaSet`
* `Deployment`
* `StatefulSet`
* `DaemonSet`
* `Job`
* `CronJob`
* `ReplicationController` (legacy)

### Networking Resources

* `Service`
* `Ingress`
* `NetworkPolicy`
* `EndpointSlice`
* `Endpoints`

### Configuration Resources

* `ConfigMap`
* `Secret`

### Storage Resources

* `PersistentVolume` (PV)
* `PersistentVolumeClaim` (PVC)
* `StorageClass`
* `VolumeAttachment`

### Access Control & Security

* `ServiceAccount`
* `Role`
* `RoleBinding`
* `ClusterRole`
* `ClusterRoleBinding`

### Cluster Administration

* `Namespace`
* `ResourceQuota`
* `LimitRange`
* `PriorityClass`
* `Lease`

### Node Resources

* `Node`

### Discovery & Metadata

* `Event`

### Autoscaling

* `HorizontalPodAutoscaler` (HPA)

### Admission & Policy

* `ValidatingAdmissionPolicy`
* `ValidatingAdmissionPolicyBinding`

---

For interviews, focus primarily on:

1. Pod
2. ReplicaSet
3. Deployment
4. Service
5. Ingress
6. ConfigMap
7. Secret
8. Namespace
9. PersistentVolume
10. PersistentVolumeClaim
11. StatefulSet
12. DaemonSet
13. Job
14. CronJob
15. ServiceAccount
16. Role / RoleBinding
17. ClusterRole / ClusterRoleBinding
18. NetworkPolicy
19. HorizontalPodAutoscaler

These cover the vast majority of real-world Kubernetes usage.
